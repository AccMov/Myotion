library(R.matlab)
library(stringr)
library(ggplot2)
library(plotly)
library(shinycssloaders)
library(ggthemes)
library(shinydashboardPlus)
library(DT)
library(shiny)
library(shinydashboard)
library(tidyverse)
library(fresh)
#library(bslib)
library(ggridges)
library(shinyWidgets)
#setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

## functions
options(shiny.port = 7775)


# read data
muscle <- rep(c("ES", "MF", "GMed", "BF", "LGM", "RA", "EO", "TFL", "RF", "TA"), times = 17)

# Groups
groupA_names <- list.files("data/Group_A", pattern="*.mat", full.names=TRUE)
groupA <- lapply(groupA_names, readMat)
groupA = unlist(groupA,recursive=FALSE)

groupB_names <- list.files("data/Group_B", pattern="*.mat", full.names=TRUE)
groupB <- lapply(groupB_names, readMat)
groupB = unlist(groupB,recursive=FALSE)



# Time domain parameters names
time_domain_para = c("MIN","MAX","MEAN","MED","SD","VAR","PP","ZC","AUC","RMS","MP","MAV","EN","WL","SK","KUR")
freq_domain_para = c("MNF","MDF","SPC","BPd","BPt","BPa","BPb","BPg")
advanced = c("FS1","FS2","FS3")
domain_list = list(time_domain_para,freq_domain_para)

domain = c("time_domain_para","freq_domain_para","advanced")




# Initial

domain_select = "time_domain_para"
para_bar = time_domain_para[3]
para_bar2 = "Non"
group_A_select = c("Results.GA.PP001","Results.GA.PP002","Results.GA.PP003","Results.GA.PP004",
                   "Results.GA.PP005","Results.GA.PP006","Results.GA.PP007","Results.GA.PP008")
group_B_select = c("Results.GB.PP001","Results.GB.PP002","Results.GB.PP003","Results.GB.PP004",
                   "Results.GB.PP005","Results.GB.PP006","Results.GB.PP007","Results.GB.PP008","Results.GB.PP009")


## Draw data

df_draw = data.frame(id = c(), muscle = c(), para = c(), value = c(), group = c())
for (i in 1:length(group_A_select)){
  ppi = groupA[which(names(groupA) == group_A_select[i])]
  domain_ppi = ppi[[1]][[which(domain==domain_select)]]
  sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar))
  
  df_bar_ppi = data.frame(id = rep(group_A_select[i], length(attr(domain_ppi,"dimnames")[[1]])), # fix the number of muscle to 10 for now
                          muscle = attr(domain_ppi,"dimnames")[[1]],
                          para = rep(para_bar, length(attr(domain_ppi,"dimnames")[[1]])),
                          value = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar)),
                          group = rep("GroupA", length(attr(domain_ppi,"dimnames")[[1]])))
  if(para_bar2!="Non"){
    df_bar_ppi$value2 = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar2))
  }
  df_draw = rbind(df_draw, df_bar_ppi)
}

for (i in 1:length(group_B_select)){
  ppi = groupB[which(names(groupB) == group_B_select[i])]
  domain_ppi = ppi[[1]][[which(domain==domain_select)]]
  sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar))
  
  df_bar_ppi = data.frame(id = rep(group_B_select[i], length(attr(domain_ppi,"dimnames")[[1]])), # fix the number of muscle to 10 for now
                          muscle = attr(domain_ppi,"dimnames")[[1]],
                          para = rep(para_bar, length(attr(domain_ppi,"dimnames")[[1]])),
                          value = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar)),
                          group = rep("GroupB", length(attr(domain_ppi,"dimnames")[[1]])))
  if(para_bar2!="Non"){
    df_bar_ppi$value2 = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar2))
  }
  df_draw = rbind(df_draw, df_bar_ppi)
}

## server
server <- function(input, output) {
  

  
  output$uiselect1 = renderUI({
    if(input$select1 == "time_domain_para"){
      choice_select2 = time_domain_para
    } else if(input$select1 == "freq_domain_para"){
      choice_select2 = freq_domain_para
    } else if(input$select1 == "advanced"){
      choice_select2 = advanced
    }
    selectInput('select2', 'Select Metrics 1', choice = choice_select2, selected = choice_select2[3])
  })
  
  output$uiselect2 = renderUI({
    if(input$select1 == "time_domain_para"){
      choice_select2 = time_domain_para
    } else if(input$select1 == "freq_domain_para"){
      choice_select2 = freq_domain_para
    } else if(input$select1 == "advanced"){
      choice_select2 = advanced
    }
    selectInput('select22', 'Select Metrics 2', choice = c("Non",choice_select2), selected = "Non")
  })
  
  output$uiselect3 = renderUI({
    if(input$select22 == "Non" & input$select1 != "advanced"){
      choice_select3 = c("Bar chart","Density plot","Boxplot")
    } else if(input$select22 != "Non" & input$select1 != "advanced"){
      choice_select3 = c("Scatter plot")
    }  else if(input$select1 == "advanced"){
      choice_select3 = c("Functional curve")
    } 
    selectInput("select3", "Select plot type", choices = choice_select3,
                selected = choice_select3[1])
  })
  
  
  output$uiselect4 = renderUI({
    muscle_name = unique(df_draw()$muscle)
    pickerInput("select4", "Two-sample t test for single/multiple muscles", choices = muscle_name,
                selected = muscle_name[1], multiple = TRUE)
  })
  
  output$uihypotest1 = renderUI({
    if((input$hypotest1)!= "Comparing Group A & Group B"){
      if(length(input$select4)==1){
        numericInput("nullinput", label = withMathJax(("Null Hypothesis $$H_0 : \\mu = $$")), 0)
      }else if(length(input$select4)>1){
        numericInput("nullinput", label = withMathJax(("Null Hypothesis $$H_0 :  \\underline{\\mu} = $$")), 0)
      }
    }else if ((input$hypotest1)== "Comparing Group A & Group B"){
      
      if(length(input$select4)==1){
        numericInput("nullinput", label = withMathJax(("Null Hypothesis $$H_0 : \\mu_1 - \\mu_2 = $$")), 0)
      }else if(length(input$select4)>1){
        numericInput("nullinput", label = withMathJax(("Null Hypothesis $$H_0 : \\underline{\\mu}_1 - \\underline{\\mu}_2 = $$")), 0)
      }
      
    }
  })
  
  output$testtext = renderUI({
    if(input$hypotest1 == "Group A"){
      selectcompar = "GroupA"
      
    }else if(input$hypotest1 == "Group B"){
      selectcompar = "GroupB"
      
    }else{
      selectcompar = c("GroupA", "GroupB")
      
    }
    
    df_test = df_draw() %>% filter(muscle %in% input$select4, group %in% selectcompar)
    test_confint <- t.test(x = df_test$value, mu = input$nullinput,
                           alternative = "two.sided", conf.level = 1 - input$hypotest3)
    test <- t.test(x = df_test$value, mu = input$nullinput,
                   alternative = input$hypotest2, conf.level = 1 - input$hypotest3)
    
    withMathJax(
      paste0("\\(n =\\) ", dim(df_test)[1], collapse = " "),
      br(),
      paste0("\\(\\bar{x} =\\) ", round(mean(df_test$value),2), collapse = " "),
      br(),
      paste0("\\(s =\\) ", round(sd(df_test$value),2), collapse = " "),
      br(),
      tags$b("Confidence interval"),
      br(),
      paste0(
        (1 - input$hypotest3) * 100, "% CI for \\(\\mu = \\bar{x} \\pm t_{\\alpha/2, n - 1} \\dfrac{s}{\\sqrt{n}} = \\) ",
        round(test_confint$estimate, 3), "  \\( \\pm \\) ", "\\( ( \\)", round(qt(input$hypotest3 / 2,
                                                                                  df = test_confint$parameter, lower.tail = FALSE), 3), " * ",
        round(test_confint$stderr * sqrt(length(df_test$value)), 3), " / ", round(sqrt(length(df_test$value)), 3), "\\( ) \\) ", "\\( = \\) ",
        "[", round(test_confint$conf.int[1], 3), "; ", round(test_confint$conf.int[2], 3), "]"
      ),
      br(),
      br(),
      tags$b("Hypothesis test"),
      br(),
      paste0("1. \\(H_0 : \\mu_D = \\) ", test$null.value, " and \\(H_1 : \\mu_D \\) ", ifelse(input$hypotest2 == "two.sided", "\\( \\neq \\) ", ifelse(input$hypotest2 == "greater", "\\( > \\) ", "\\( < \\) ")), test$null.value),
      br(),
      paste0(
        "2. Test statistic : \\(t_{obs} = \\dfrac{\\bar{D} - \\mu_0}{s_D / \\sqrt{n}} = \\) ",
        "(", round(test$estimate, 3), ifelse(test$null.value >= 0, paste0(" - ", test$null.value), paste0(" + ", abs(test$null.value))), ") / ", round(test$stderr, 3), " \\( = \\) ",
        round(test$statistic, 3)
      ),
      br(),
      paste0(
        "3. Critical value :", ifelse(input$hypotest2 == "two.sided", " \\( \\pm t_{\\alpha/2, n - 1} = \\pm t(\\)", ifelse(input$hypotest2 == "greater", " \\( t_{\\alpha, n - 1} = t(\\)", " \\( -t_{\\alpha, n - 1} = -t(\\)")),
        ifelse(input$hypotest2 == "two.sided", input$hypotest3 / 2, input$hypotest3), ", ", test$parameter, "\\()\\)", " \\( = \\) ",
        ifelse(input$hypotest2 == "two.sided", "\\( \\pm \\)", ifelse(input$hypotest2 == "greater", "", " -")),
        ifelse(input$hypotest2 == "two.sided", round(qt(input$hypotest3 / 2, df = test$parameter, lower.tail = FALSE), 3), round(qt(input$hypotest3, df = test$parameter, lower.tail = FALSE), 3))
      ),
      br(),
      paste0("4. Conclusion : ", ifelse(test$p.value < input$hypotest3, "Reject \\(H_0\\)", "Do not reject \\(H_0\\)")),
      br(),
      br()
    )
    
  })
  
  
  
  output$uiplot1 = renderUI({
    if(input$select3 != "Density plot"){
      plotlyOutput("plotly_A")  %>% withSpinner(color="orange")
    } else if(input$select3 == "Density plot") {
      plotOutput("plot_A")  %>% withSpinner(color="orange")
    }
  })
  

  
  output$plotoption = renderUI({
    if(input$select3 %in% c("Bar chart","Boxplot","Scatter plot")){
      checkboxInput("singleplot","Single plot", FALSE)

    }
  })
  
  
  
  df_draw <- reactive({
    domain_select = input$select1
    para_bar = input$select2
    para_bar2 = input$select22
    group_A_select = input$filterA2 
    group_B_select = input$filterB2
    
    
    ## Draw data
    
    df_draw = data.frame(id = c(), muscle = c(), para = c(), value = c(), group = c())
    for (i in 1:length(group_A_select)){
      ppi = groupA[which(names(groupA) == group_A_select[i])]
      domain_ppi = ppi[[1]][[which(domain==domain_select)]]
      sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar))
      
      df_bar_ppi = data.frame(id = rep(group_A_select[i], length(attr(domain_ppi,"dimnames")[[1]])), # fix the number of muscle to 10 for now
                              muscle = attr(domain_ppi,"dimnames")[[1]],
                              para = rep(para_bar, length(attr(domain_ppi,"dimnames")[[1]])),
                              value = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar)),
                              group = rep("GroupA", length(attr(domain_ppi,"dimnames")[[1]])))
      if(para_bar2!="Non"){
        df_bar_ppi$value2 = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar2))
      }
      df_draw = rbind(df_draw, df_bar_ppi)
    }
    
    for (i in 1:length(group_B_select)){
      ppi = groupB[which(names(groupB) == group_B_select[i])]
      domain_ppi = ppi[[1]][[which(domain==domain_select)]]
      sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar))
      
      df_bar_ppi = data.frame(id = rep(group_B_select[i], length(attr(domain_ppi,"dimnames")[[1]])), # fix the number of muscle to 10 for now
                              muscle = attr(domain_ppi,"dimnames")[[1]],
                              para = rep(para_bar, length(attr(domain_ppi,"dimnames")[[1]])),
                              value = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar)),
                              group = rep("GroupB", length(attr(domain_ppi,"dimnames")[[1]])))
      if(para_bar2!="Non"){
        df_bar_ppi$value2 = sapply(domain_ppi,"[[",which(domain_list[[which(domain==domain_select)]] == para_bar2))
      }
      df_draw = rbind(df_draw, df_bar_ppi)
    }
    df_draw
    
  })
  
  
  df_draw_f <- reactive({
    domain_select = input$select1
    para_bar = input$select2
    para_bar2 = input$select22
    group_A_select = input$filterA2 
    group_B_select = input$filterB2
    
    
    ## Draw data
    
    df_draw_f = data.frame(id = c(), FS = c(), Time_index = c(), value = c(), group = c())
    for (i in 1:length(group_A_select)){
      ppi = groupA[which(names(groupA) == group_A_select[i])]
      domain_ppi = ppi[[1]][[which(domain==domain_select)]]
      
      ts_ppi = domain_ppi[[2]]
      down_sample = seq(from = 1, to = length(ts_ppi[1,]),length.out = 3000)
      ts_ppi = ts_ppi[,down_sample]
      rownames(ts_ppi) = c("FS1","FS2","FS3")
      df_bar_ppi = data.frame(id = rep(group_A_select[i], length(down_sample)), # fix the number of muscle to 10 for now
                              FS = rep(para_bar, length(down_sample)),
                              Time_index = 1:length(down_sample),
                              value = ts_ppi[which(rownames(ts_ppi) == para_bar),],
                              group = rep("GroupA", length(down_sample)))
      if(para_bar2!="Non"){
        df_bar_ppi$value2 =  ts_ppi[which(rownames(ts_ppi) == para_bar2),]
      }
      df_draw_f = rbind(df_draw_f, df_bar_ppi)
    }
    
    for (i in 1:length(group_B_select)){
      ppi = groupB[which(names(groupB) == group_B_select[i])]
      domain_ppi = ppi[[1]][[which(domain==domain_select)]]
      
      ts_ppi = domain_ppi[[2]]
      down_sample = seq(from = 1, to = length(ts_ppi[1,]),length.out = 3000)
      ts_ppi = ts_ppi[,down_sample]
      rownames(ts_ppi) = c("FS1","FS2","FS3")
      df_bar_ppi = data.frame(id = rep(group_B_select[i], length(down_sample)), # fix the number of muscle to 10 for now
                              FS = rep(para_bar, length(down_sample)),
                              Time_index = 1:length(down_sample),
                              value = ts_ppi[which(rownames(ts_ppi) == para_bar),],
                              group = rep("GroupB", length(down_sample)))
      if(para_bar2!="Non"){
        df_bar_ppi$value2 =  ts_ppi[which(rownames(ts_ppi) == para_bar2),]
      }
      df_draw_f = rbind(df_draw_f, df_bar_ppi)
    }
    df_draw_f
    
  })
  
  output$testdata = DT::renderDataTable({
    if(input$hypotest1 == "Group A"){
      selectcompar = "GroupA"
      
    }else if(input$hypotest1 == "Group B"){
      selectcompar = "GroupB"
      
    }else{
      selectcompar = c("GroupA", "GroupB")
      
    }
    df_test = df_draw() %>% filter(muscle %in% input$select4, group %in% selectcompar)
    DT::datatable({df_test})
  })

  
  
  output$testplot = renderPlot({
    
    if(input$hypotest1 == "Group A"){
      selectcompar = "GroupA"
      
    }else if(input$hypotest1 == "Group B"){
      selectcompar = "GroupB"
      
    }else{
      selectcompar = c("GroupA", "GroupB")
      
    }
    
    df_test = df_draw() %>% filter(muscle %in% input$select4, group %in% selectcompar)
    
    test <- t.test(x = df_test$value, mu = input$nullinput,
                   alternative = input$hypotest2, conf.level = 1 - input$hypotest3)    
    
    p <- ggplot(data.frame(x = c(qt(0.999, df = test$parameter, lower.tail = FALSE), qt(0.999, df = test$parameter, lower.tail = TRUE))), aes(x = x)) +
      stat_function(fun = dt, args = list(df = test$parameter)) +
      theme_minimal() +
      geom_vline(xintercept = test$statistic, color = "steelblue") +
      geom_text(aes(x = test$statistic, label = paste0("Test statistic = ", round(test$statistic, 3)), y = 0.2),
                colour = "steelblue", angle = 90, vjust = 1.3) +
      ggtitle(paste0("Student distribution", " t(", round(test$parameter, 3), ")")) +
      theme(plot.title = element_text(face = "bold", hjust = 0.5)) +
      ylab("Density") +
      xlab("x")
    
    if(test$alternative == "two.sided"){
      funcShaded_twoside <- function(x) {
        y <- dt(x, df = test$parameter)
        y[x < qt(input$hypotest3 / 2, df = test$parameter, lower.tail = FALSE) & x > qt(input$hypotest3 / 2, df = test$parameter) ] <- NA
        return(y)
      }
      p+stat_function(fun = funcShaded_twoside, geom = "area", alpha = 0.6)
    }else if(test$alternative == "less"){
      funcShaded_less <- function(x) {
        y <- dt(x, df = test$parameter)
        y[x > qt(input$hypotest3, df = test$parameter, lower.tail = TRUE) ] <- NA
        return(y)
      }
      p+stat_function(fun = funcShaded_less, geom = "area", alpha = 0.6)
      
    }else if(test$alternative == "greater"){
      funcShaded_greater <- function(x) {
        y <- dt(x, df = test$parameter)
        y[x < qt(input$hypotest3,  df = test$parameter, lower.tail = FALSE) ] <- NA
        return(y)
      }
      p+stat_function(fun = funcShaded_greater, geom = "area", alpha = 0.6)
      
    }
    
    
   
    
    
    
    
  })
  output$plotly_A = renderPlotly({
    
    if(length(input$singleplot) == 0){
      
      df_bar = df_draw() %>% dplyr::group_by(group, muscle) %>%
        summarise(sd = sd(value),
                  Average = mean(value),
                  Min = min(value),
                  Max = max(value),
                  Median = median(value)
        )
      
      bar_plot = ggplot(df_bar, aes(x=muscle, y= Average, fill=group)) + 
        facet_wrap(~ group, scales = "free_x") + 
        geom_col(alpha = 0.6) + 
        labs(
          x = "Muscle names",
          y = "Average parameter values",
          subtitle = ""
        )+
        scale_y_continuous(expand = c(0, 0)) +
        theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
        theme(text = element_text(size = 20),
              axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1),
              legend.position = "none") +
        guides(fill=guide_legend(title="")) 
      ggplotly(bar_plot)%>%
        layout(legend = list(
          orientation = "h", xanchor = "center", x = 0.5, y= 1
        ))
      
    }else{
    ## Draw plot
    if(input$select3 == "Bar chart"){
      if(!input$singleplot){
        df_bar = df_draw() %>% dplyr::group_by(group, muscle) %>%
          summarise(sd = sd(value),
                    Average = mean(value),
                    Min = min(value),
                    Max = max(value),
                    Median = median(value)
          )
        
        bar_plot = ggplot(df_bar, aes(x=muscle, y= Average, fill=group)) + 
          facet_wrap(~ group, scales = "free_x") + 
          geom_col(alpha = 0.6) + 
          labs(
            x = "Muscle names",
            y = "Average parameter values",
            subtitle = ""
          )+
          scale_y_continuous(expand = c(0, 0)) +
          theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
          theme(text = element_text(size = 20),
                axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1),
                legend.position = "none") +
          guides(fill=guide_legend(title="")) 
      } else{
        df_bar = df_draw() %>% dplyr::group_by(group, muscle) %>%
          summarise(sd = sd(value),
                    Average = mean(value),
                    Min = min(value),
                    Max = max(value),
                    Median = median(value)
          )
        
        bar_plot = ggplot(df_bar, aes(x=muscle, y= Average, fill=group)) + 
          geom_bar(stat = "identity",  width = 0.6, alpha = 0.6,
                   position=position_dodge(width = 0.6)) + 
          scale_y_continuous(expand = c(0, 0) ) +
          labs(
            x = "Muscle names",
            y = "Average parameter values",
            subtitle = ""
          )+
          theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
          theme(text = element_text(size = 20),
                legend.position = "top") +
          guides(fill=guide_legend(title=""))
      }
      
      ggplotly(bar_plot)%>%
        layout(legend = list(
          orientation = "h", xanchor = "center", x = 0.5, y= 1
        ))
      
    } else if(input$select3 == "Boxplot"){
      df_box = df_draw()
      df_box$group = as.factor(df_box$group)
      
      if(input$singleplot){

      fig = plot_ly(df_box, x = ~muscle, y = ~value, color = ~group, type = "box", 
                    colors = c("red", "blue")) %>% layout(boxmode = "group",
                                                          xaxis = list(tickfont = list(size = 20)), 
                                                          yaxis = list(tickfont = list(size = 20)))%>%
        layout(legend = list(
          orientation = "h", xanchor = "center", x = 0.5, y= 1
        ))
      } else{
        fig = df_box %>%
          group_by(group) %>%
          do(p=plot_ly(., x = ~muscle, y = ~value, color = ~ group, type = "box",
                       colors = c("red", "blue"))) %>%
          subplot(nrows = 1, shareX = TRUE, shareY = TRUE)%>%
          layout(legend = list(
            orientation = "h", xanchor = "center", x = 0.5, y= 1
          ))
        
      }
      fig
    } else if(input$select3 == "Scatter plot"){
      df_scat = df_draw()
      
      if(input$singleplot){

      scat_plot = ggplot(df_scat) + 
        geom_point(size=4, alpha = 0.6,
                   aes(x=value, y=value2, color=group,
                       text = paste("Muscle:", muscle, "\nID:",id))) +
        geom_smooth(method="lm" , se=TRUE,
                    aes(x = value, y = value2, color = group, fill = group))+
        theme_tufte()+ 
        facet_wrap(~ group, scales = "free_x")+
        labs(
          x = para_bar,
          y = para_bar2,
          subtitle = ""
        )+
        theme(text = element_text(size = 20),
              legend.position = "none")
      } else{
        scat_plot = ggplot(df_scat) + 
          geom_point(size=4, alpha = 0.6,
                     aes(x=value, y=value2, color=group,
                         text = paste("Muscle:", muscle, "\nID:",id))) +
          geom_smooth(method="lm" , se=TRUE,
                      aes(x = value, y = value2, color = group, fill = group))+
          theme_tufte()+ 
          labs(
            x = para_bar,
            y = para_bar2,
            subtitle = ""
          )+
          theme(text = element_text(size = 20),
                legend.position = "top") +
          guides(color=guide_legend(title=""),
                 fill=FALSE) 
      }
      
      ggplotly(scat_plot)%>%
        layout(legend = list(
          orientation = "h", xanchor = "center", x = 0.5, y= 1
        ))
      
      
    } 
    else if(input$select3 == "Functional curve"){
      df_scat = df_draw_f()
      mean_curve = df_scat %>% group_by(group,Time_index) %>% summarise(value = mean(value)) %>%
        ungroup() %>%
        mutate(id = c(rep("GroupAMean",3000),rep("GroupBMean",3000)),
               FS = rep(input$select2,2*3000))
      time_plot = ggplot(df_scat, aes(x = Time_index, y = value, group = id,color = group,
                                      text = paste("FS:", FS, "\nID:",id))) + 
        geom_line(alpha = 0.2,size = 1) + theme_minimal() +
        geom_line(data = mean_curve,
                  aes(x = Time_index, y = value, group = id,color = group), alpha = 1 ,size = 1.5)+
        ggtitle(input$select2) +
        xlab("Time index") + ylab("Value")+
        facet_wrap(~ group, scales = "free_x")+
        theme(panel.spacing.x = unit(0, "mm")) +
        theme(text = element_text(size = 20),
              legend.position = "none") 
      
      ggplotly(time_plot)
      
    } }
  })
 
  
  output$plot_A = renderPlot({
    df_dens = df_draw()
    
    dens_plot = ggplot(df_dens, aes(x = value, y = muscle, fill = group,color = group)) + 
      geom_density_ridges( alpha = 0.5) + 
      facet_wrap(~ group, scales = "free_x")+
      theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
      theme(text = element_text(size = 20),
            legend.position = "none") 
    
    dens_plot
    
  })
  
  output$DTtable1 <- DT::renderDataTable({
    
    
    ## Draw plot
    if(input$select3 == "Bar chart"){
      dt_table = df_draw() %>% dplyr::group_by(group, muscle) %>%
        summarise(sd = sd(value),
                  Average = mean(value),
                  Min = min(value),
                  Max = max(value),
                  Median = median(value)
        )
      rg = range(dt_table$Average)
      loc_value = which(names(dt_table) == "Average")
    } else if(input$select3 == "Boxplot"){
      dt_table = df_draw()
      rg = range(dt_table$value)
      loc_value = which(names(dt_table) == "value")
      
      
    } else if(input$select3 == "Scatter plot"){
      dt_table = df_draw()
      rg = range(dt_table$value)
      loc_value = which(names(dt_table) == "value")
      
      
      
    } 
    else if(input$select3 == "Density plot"){
      dt_table = df_draw()
      rg = range(dt_table$value)
      loc_value = which(names(dt_table) == "value")
      
      
      
    } 
    else if(input$select3 == "Functional curve"){
      dt_table = df_draw_f()

    }
    
    DT::datatable({dt_table},
                  extensions = 'Buttons',
                  options = list(
                    paging = TRUE,
                    searching = TRUE,
                    scrollX=F, 
                    fixedColumns = TRUE,
                    autoWidth = TRUE,
                    ordering = TRUE,
                    dom = 'Blfrtip',
                    buttons = c('copy', 'csv', 'excel', 'pdf'),
                    lengthMenu=list(c(10, -1), c('10', 'All'))), rownames= FALSE) 
    
  })
  
  
}
