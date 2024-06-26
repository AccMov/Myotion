pacs = c("R.matlab","stringr","ggplot2","plotly","shinycssloaders",
          "ggthemes","shinydashboardPlus","DT","shiny","shinydashboard",
          "tidyverse","flextable","fresh","rempsyc","ggridges","shinyWidgets","shinyjs",
         "xtable","kableExtra","car","XML","viridis","svSocket")

lapply(pacs, require, character.only = TRUE)


#setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
# Define a function to handle client connections
path = NULL
## server
server <- function(input, output) {
  
  
  handle_client <- function(msg, client, port) {
    #cat("Client:", client, ":", port, " connected.\n")
    # Read data from the client
    cat("Received from client:", msg, "\n")
    # Close the connection
    cat("Client connection closed.\n")
    path <<- msg
    return(0)
  }
  
  
  svSocket::startSocketServer(
    port = 7776,
    procfun = handle_client ,
    secure = FALSE,
    local = TRUE
  )
  #print(path)
  while(is.null(path)){
    Sys.sleep(3)
  print(path)
  oldpath <<- path
  }
  
  ## functions
  #a =while (TRUE) {}
  groupA_names <- list.files(path, pattern="*.xml", full.names=TRUE)
  groupA <- lapply(groupA_names, xmlToList)
  
  for(i in 1:length(groupA)){
    names(groupA)[i] = groupA[[i]]$Person$name
  }
  
  # read data
  muscle_name = c(names(groupA$ABC1$emg$timeSeriesTable$channels))
  
  # Time domain parameters names
  time_domain_para = names(groupA$ABC1$emg$statistic)[1:13]
  freq_domain_para = names(groupA$ABC1$emg$statistic)[14:20]
  advanced = names(groupA$ABC1$emg$timeSeriesTable$channels)
  domain_list = list(time_domain_para,freq_domain_para)
  
  domain = c("time_domain_para","freq_domain_para","advanced")
  
  
  
  
  # Initial
  
  domain_select = "time_domain_para"
  para_bar = time_domain_para[3]
  para_bar2 = "Non"
  group_A_select = c("ABC1","ABC2","ABC3","ABC4")
  group_B_select = c("ABC1","ABC2","ABC3","ABC4")
  
  
  ## Draw data
  
  df_draw = data.frame(id = c(), muscle = c(), para = c(), value = c(), group = c())
  for (i in 1:length(group_A_select)){
    ppi = groupA[which(names(groupA) == group_A_select[i])]
    domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
    domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
    df_bar_ppi = data.frame(id = rep(group_A_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                            muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                            para = rep(para_bar, length(domain_ppi)),
                            value = domain_ppi,
                            group = rep("GroupA", length(domain_ppi)))
    if(para_bar2!="Non"){
      domain_ppi2 = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar2)]]
      domain_ppi2 = as.numeric(strsplit(domain_ppi2,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi$value2 = domain_ppi2
    }
    df_draw = rbind(df_draw, df_bar_ppi)
  }
  
  for (i in 1:length(group_B_select)){
    ppi = groupA[which(names(groupA) == group_B_select[i])]
    domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
    domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
    df_bar_ppi = data.frame(id = rep(group_B_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                            muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                            para = rep(para_bar, length(domain_ppi)),
                            value = domain_ppi,
                            group = rep("GroupB", length(domain_ppi)))
    if(para_bar2!="Non"){
      domain_ppi2 = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar2)]]
      domain_ppi2 = as.numeric(strsplit(domain_ppi2,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi$value2 = domain_ppi2
    }
    df_draw = rbind(df_draw, df_bar_ppi)
  }
  
  observeEvent(path!=oldpath, {
    oldpath <<- path
    #a =while (TRUE) {}
    groupA_names <- list.files(path, pattern="*.xml", full.names=TRUE)
    groupA <- lapply(groupA_names, xmlToList)
    
    for(i in 1:length(groupA)){
      names(groupA)[i] = groupA[[i]]$Person$name
    }
    
    # read data
    muscle_name = c(names(groupA$ABC1$emg$timeSeriesTable$channels))
    
    # Time domain parameters names
    time_domain_para = names(groupA$ABC1$emg$statistic)[1:13]
    freq_domain_para = names(groupA$ABC1$emg$statistic)[14:20]
    advanced = names(groupA$ABC1$emg$timeSeriesTable$channels)
    domain_list = list(time_domain_para,freq_domain_para)
    
    
  })
  
  observeEvent(input$goButton, {
    oldpath <<- path
    #a =while (TRUE) {}
    groupA_names <- list.files(path, pattern="*.xml", full.names=TRUE)
    groupA <- lapply(groupA_names, xmlToList)
    
    for(i in 1:length(groupA)){
      names(groupA)[i] = groupA[[i]]$Person$name
    }
    
    # read data
    muscle_name = c(names(groupA$ABC1$emg$timeSeriesTable$channels))
    
    # Time domain parameters names
    time_domain_para = names(groupA$ABC1$emg$statistic)[1:13]
    freq_domain_para = names(groupA$ABC1$emg$statistic)[14:20]
    advanced = names(groupA$ABC1$emg$timeSeriesTable$channels)
    domain_list = list(time_domain_para,freq_domain_para)
  })

  output$out1 <- renderUI({

    if (input$tab == "tests") {

      
        dyn_ui <- list(selectInput("testselect2", "Select domain ", choices = domain,
                                   selected = "time_domain_para"),
                       uiOutput('testuiselect1'),
                       pickerInput("testselect4", "Select muscles", choices = muscle_name,
                                     selected = muscle_name[1], multiple = F))
        
      
    } 
    if (input$tab == "groups") {
      
      dyn_ui <- list(  selectInput("select1", "Select domain ", choices = domain,
                                   selected = "time_domain_para"),
                       uiOutput('uiselect1'),
                       uiOutput('uiselect2'),
                       uiOutput('uiselect3'),
                       actionButton("goButton", "Generate figure"),
                       tabsetPanel(id = "tabset_id1", selected = "t1", 
                                   tabPanel("Advanced options",  value = "t3",
                                            uiOutput("plotoption")))
                       
      )
    }
    return(dyn_ui)
  })
  
  output$testtype <- renderUI({
    dt_test = df_draw_test()
    if (input$tab == "tests") {
      if(length(unique(dt_test$group))==2){
        return(list(selectInput("testselect1", "Select test ", choices = c("Two sample t test"),
                           selected = "Two sample t test"),
                    tabsetPanel(id = "tabset_id2", selected = "tt1", 
                                tabPanel("Advanced options",  value = "tt3",
                                         selectInput("somethinghere", "Some useful options", choices = c("1","2","3"),
                                                     selected = "1")))))
        
      } else if(length(unique(dt_test$group))>2){
        return(list(selectInput("testselect1", "Select test ", choices = c("One-way ANOVA","Tukey's HSD"),
                           selected = "One-way ANOVA"),
                    tabsetPanel(id = "tabset_id2", selected = "tt1", 
                                tabPanel("Advanced options",  value = "tt3",
                                         selectInput("somethinghere", "Some useful options", choices = c("1","2","3"),
                                                     selected = "1")))
                    ))
      }

    } 
    if (input$tab == "groups") {
      
    }
  })
  
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
  
  output$testuiselect1 = renderUI({
    if(input$testselect2 == "time_domain_para"){
      tchoice_select2 = time_domain_para
    } else if(input$testselect2 == "freq_domain_para"){
      tchoice_select2 = freq_domain_para
    } else if(input$testselect2 == "advanced"){
      tchoice_select2 = advanced
    }
    selectInput('testselect3', 'Select Metrics', choice = tchoice_select2,
                selected = tchoice_select2[3],multiple = T)
  })
  

  

  
  
  
  output$uiplot1 = renderUI({
      plotlyOutput("plotly_A")  %>% withSpinner(color="orange")
  })
  

  
  output$plotoption = renderUI({

    if(input$select3 %in% c("Bar chart","Boxplot","Scatter plot", "Density plot")){
      figure_option_ui = list(
        checkboxInput("singleplot","Single plot", FALSE),
        textInput("title_input", "Title", value = ""),
        textInput("y_input", "Y label", value = ""),
        textInput("x_input", "X label", value = ""),
        sliderInput("titlesize", "Title font size", value = 20, min = 1, max = 80),
        sliderInput("xylabelsize", "x & y label size", value = 15, min = 1, max = 80),
        sliderInput("xytextsize", "xy-axis text size", value = 10, min = 1, max = 50),
        selectInput("plotcolor","Color palettes", choices = c("Regular","Black & White","Color blind friendly"), selected = "Regular")

      )
    }

    
    return(figure_option_ui)
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
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_A_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("GroupA", length(domain_ppi)))
      if(para_bar2!="Non"){
        domain_ppi2 = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar2)]]
        domain_ppi2 = as.numeric(strsplit(domain_ppi2,split=" ",fixed=TRUE)[[1]])
        df_bar_ppi$value2 = domain_ppi2
      }
      df_draw = rbind(df_draw, df_bar_ppi)
      
    }
    
    for (i in 1:length(group_B_select)){
      ppi = groupA[which(names(groupA) == group_B_select[i])]
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_B_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("GroupB", length(domain_ppi)))
      if(para_bar2!="Non"){
        domain_ppi2 = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar2)]]
        domain_ppi2 = as.numeric(strsplit(domain_ppi2,split=" ",fixed=TRUE)[[1]])
        df_bar_ppi$value2 = domain_ppi2
      }
      df_draw = rbind(df_draw, df_bar_ppi)
      
    }
    df_draw
    
  })
  
  df_draw_test <- reactive({
    domain_select = input$testselect2
    para_bar_seq = input$testselect3
    para_bar2 = "Non"
    group_1_select = input$filter12 
    group_2_select = input$filter22
    group_3_select = input$filter32 
    group_4_select = input$filter42
    group_5_select = input$filter52 
    group_6_select = input$filter62
    
    ## Draw data
    df_draw_test_all = c()
    for(j in 1:length(para_bar_seq)){
      para_bar = para_bar_seq[j]
    df_draw_test = data.frame(id = c(), muscle = c(), para = c(), value = c(), group = c())
    if(length(group_1_select)>0){for (i in 1:length(group_1_select)){
      
      ppi = groupA[which(names(groupA) == group_1_select[i])]
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_1_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("Group 1", length(domain_ppi)))
      df_draw_test = rbind(df_draw_test, df_bar_ppi)
      
    }}
    
    if(length(group_2_select)>0){for (i in 1:length(group_2_select)){
      
      ppi = groupA[which(names(groupA) == group_2_select[i])]
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_2_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("Group 2", length(domain_ppi)))
      df_draw_test = rbind(df_draw_test, df_bar_ppi)
      
    }}
    
    if(length(group_3_select)>0){for (i in 1:length(group_3_select)){
      
      ppi = groupA[which(names(groupA) == group_3_select[i])]
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_3_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("Group 3", length(domain_ppi)))
      df_draw_test = rbind(df_draw_test, df_bar_ppi)
      
    }}
    
    if(length(group_4_select)>0){for (i in 1:length(group_4_select)){
      
      ppi = groupA[which(names(groupA) == group_4_select[i])]
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_4_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("Group 4", length(domain_ppi)))
      df_draw_test = rbind(df_draw_test, df_bar_ppi)
      
    }}
    
    if(length(group_5_select)>0){for (i in 1:length(group_5_select)){
      
      ppi = groupA[which(names(groupA) == group_5_select[i])]
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_5_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("Group 5", length(domain_ppi)))
      df_draw_test = rbind(df_draw_test, df_bar_ppi)
      
    }}
    
    if(length(group_6_select)>0){for (i in 1:length(group_6_select)){
      
      ppi = groupA[which(names(groupA) == group_6_select[i])]
      domain_ppi = ppi[[1]]$emg$statistic[[which(names(ppi[[1]]$emg$statistic)==para_bar)]]
      domain_ppi = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      df_bar_ppi = data.frame(id = rep(group_6_select[i], length(domain_ppi)), # fix the number of muscle to 10 for now
                              muscle = names(ppi[[1]]$emg$timeSeriesTable$channels),
                              para = rep(para_bar, length(domain_ppi)),
                              value = domain_ppi,
                              group = rep("Group 6", length(domain_ppi)))
      df_draw_test = rbind(df_draw_test, df_bar_ppi)
      
    }}
    df_draw_test_all = rbind(df_draw_test_all, df_draw_test)
    }
    
    df_draw_test = df_draw_test_all
  
    if(dim(df_draw_test)[1]>0){
      df_draw_test = df_draw_test %>% filter(muscle == input$testselect4)
    }
    
    df_draw_test
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
      domain_ppi = ppi[[1]]$emg$timeSeriesTable$channels
      domain_ppi = as.data.frame(domain_ppi)
      as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])
      domain_ppi[,1] = as.numeric(strsplit(domain_ppi,split=" ",fixed=TRUE)[[1]])

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
      ppi = groupA[which(names(groupA) == group_B_select[i])]
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



  output$plotly_A = renderPlotly({
    input$goButton
    isolate({
    if(length(input$singleplot) == 0){
      single_plot = F
    }else{
      single_plot = input$singleplot
    }


    ## Draw plot
    if(input$select3 == "Bar chart"){
      df_bar = df_draw() %>% dplyr::group_by(group, muscle) %>%
        summarise(sd = sd(value),
                  Average = mean(value),
                  Min = min(value),
                  Max = max(value),
                  Median = median(value)
        )
      if(!single_plot){

        bar_plot = ggplot(df_bar, aes(x=muscle, y= Average, fill=group)) + 
          facet_wrap(~ group, scales = "free_x") + 
          geom_col(alpha = 0.6) + 
          labs(
            x = input$x_input,
            y = input$y_input,
            title = input$title_input
          )+
          scale_y_continuous(expand = c(0, 0)) +
          theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
          theme(axis.title = element_text(size = input$xylabelsize),
                title = element_text(size = input$titlesize),
                axis.text = element_text(size = input$xytextsize),
                axis.text.x = element_text(angle = 30, vjust = 0.5, hjust=1),
                legend.position = "none") +
          guides(fill=guide_legend(title="")) 
      } else{

        bar_plot = ggplot(df_bar, aes(x=muscle, y= Average, fill=group)) + 
          geom_bar(stat = "identity",  width = 0.6, alpha = 0.6,
                   position=position_dodge(width = 0.6)) + 
          scale_y_continuous(expand = c(0, 0) ) +
          labs(
            x = input$x_input,
            y = input$y_input,
            title = input$title_input
          )+
          theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
          theme(axis.title = element_text(size = input$xylabelsize),
                title = element_text(size = input$titlesize),
                axis.text = element_text(size = input$xytextsize),
                legend.position = "top") +
          guides(fill=guide_legend(title=""))
      }
      
      if(input$plotcolor == "Black & White"){
        bar_plot = bar_plot + scale_fill_grey()
      } else if(input$plotcolor == "Color blind friendly"){
        bar_plot = bar_plot + scale_fill_viridis(discrete = T)
      }else if(input$plotcolor == "Regular"){
        bar_plot = bar_plot 
      }

      ggplotly(bar_plot)%>%
        layout(legend = list(
          orientation = "h", xanchor = "center", x = 0.5, y= 1
        ))

    } else if(input$select3 == "Boxplot"){
      df_box = df_draw()
      df_box$group = as.factor(df_box$group)

      if(single_plot){
        if(input$plotcolor == "Black & White"){
          fig = plot_ly(df_box, x = ~muscle, y = ~value, color = ~group, type = "box", colors = c("#F0F0F0","#BDBDBD"))
        } else if(input$plotcolor == "Color blind friendly"){
          fig = plot_ly(df_box, x = ~muscle, y = ~value, color = ~group, type = "box", colors = c("#fde725","#440154"))
        }else if(input$plotcolor == "Regular"){
          fig = plot_ly(df_box, x = ~muscle, y = ~value, color = ~group, type = "box", colors = c("#F8766D","#00BFC4"))
        }
        
      fig = fig %>%
        layout(boxmode = "group")%>%
        layout(legend = list(
          orientation = "h", xanchor = "center", x = 0.5, y= 1
        )) %>%
        layout(title = list(text = input$title_input, font=list(size = input$titlesize)))%>%
        layout(xaxis = list(title = input$x_input,titlefont = list(size = input$xylabelsize), tickfont = list(size = input$xytextsize)),
               yaxis = list(title = input$y_input,titlefont = list(size = input$xylabelsize), tickfont = list(size = input$xytextsize)))
      
      } else{
        if(input$plotcolor == "Black & White"){
          fig = df_box %>%
            group_by(group) %>%
            do(p=plot_ly(., x = ~muscle, y = ~value, color = ~ group, type = "box", colors = c("#F0F0F0","#BDBDBD")))
        } else if(input$plotcolor == "Color blind friendly"){
          fig = df_box %>%
            group_by(group) %>%
            do(p=plot_ly(., x = ~muscle, y = ~value, color = ~ group, type = "box", colors = c("#fde725","#440154")))
        }else if(input$plotcolor == "Regular"){
          fig = df_box %>%
            group_by(group) %>%
            do(p=plot_ly(., x = ~muscle, y = ~value, color = ~ group, type = "box", colors = c("#F8766D","#00BFC4")))
        }
        
        
        fig = fig %>%
          subplot(nrows = 1, shareX = TRUE, shareY = TRUE)%>%
          layout(legend = list(
            orientation = "h", xanchor = "center", x = 0.5, y= 1
          )) %>%
          layout(title = list(text = input$title_input, font=list(size = input$titlesize)))%>%
          layout(xaxis = list(title = input$x_input,titlefont = list(size = input$xylabelsize), tickfont = list(size = input$xytextsize)),
                 yaxis = list(title = input$y_input,titlefont = list(size = input$xylabelsize), tickfont = list(size = input$xytextsize)),
                 xaxis2 = list(title = input$x_input,titlefont = list(size = input$xylabelsize), tickfont = list(size = input$xytextsize)),
                 yaxis2 = list(title = input$y_input,titlefont = list(size = input$xylabelsize), tickfont = list(size = input$xytextsize)))

      }
      
      
      
      fig
    } else if(input$select3 == "Scatter plot"){
      df_scat = df_draw()

      if(!single_plot){

      scat_plot = ggplot(df_scat) + 
        geom_point(size=4, alpha = 0.6,
                   aes(x=value, y=value2, color=group,
                       text = paste("Muscle:", muscle, "\nID:",id))) +
        geom_smooth(method="lm" , se=F,
                    aes(x = value, y = value2, color = group, fill = group))+
        theme_tufte()+ 
        facet_wrap(~ group, scales = "free_x")+
        labs(
          x = input$x_input,
          y = input$y_input,
          title = input$title_input
        )+
        theme(axis.title = element_text(size = input$xylabelsize),
              title = element_text(size = input$titlesize),
              axis.text = element_text(size = input$xytextsize),
              legend.position = "none")
      } else{
        scat_plot = ggplot(df_scat) + 
          geom_point(size=4, alpha = 0.6,
                     aes(x=value, y=value2, color=group,
                         text = paste("Muscle:", muscle, "\nID:",id))) +
          geom_smooth(method="lm" , se=F,
                      aes(x = value, y = value2, color = group, fill = group))+
          theme_tufte()+ 
          labs(
            x = input$x_input,
            y = input$y_input,
            title = input$title_input
          )+
          theme(axis.title = element_text(size = input$xylabelsize),
                title = element_text(size = input$titlesize),
                axis.text = element_text(size = input$xytextsize),
                legend.position = "top") +
          guides(color=guide_legend(title=""),
                 fill=FALSE) 
      }

      if(input$plotcolor == "Black & White"){
        scat_plot = scat_plot + scale_color_grey()
      } else if(input$plotcolor == "Color blind friendly"){
        scat_plot = scat_plot + scale_color_viridis(discrete = T)
      } else if(input$plotcolor == "Regular"){
        scat_plot = scat_plot + scale_color_brewer(palette = "RdBu")
      }
      
      
      ggplotly(scat_plot)%>%
        layout(legend = list(
          orientation = "h", xanchor = "center", x = 0.5, y= 1
        ))
      
      
    } 
    else if(input$select3 == "Density plot"){
      df_dens = df_draw()
      dens_plot = ggplot(df_dens, aes(x = value, fill = group,color = group)) + 
        geom_density( alpha = 0.5) + 
        facet_wrap(~ muscle, scales = "free_x")+
        theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
        theme(axis.title = element_text(size = input$xylabelsize),
              title = element_text(size = input$titlesize),
              axis.text = element_text(size = input$xytextsize),
              legend.position = "none") +
        labs(
          x = input$x_input,
          y = input$y_input,
          title = input$title_input
        )
      
      if(!single_plot){
        dens_plot = dens_plot+facet_wrap(~ group+muscle, scales = "free_x")
      } 
      
      if(input$plotcolor == "Black & White"){
        dens_plot = dens_plot + scale_fill_grey() + scale_color_grey()
      } else if(input$plotcolor == "Color blind friendly"){
        dens_plot = dens_plot + scale_fill_viridis(discrete = T) + scale_color_viridis(discrete = T)
      } else if(input$plotcolor == "Regular"){
        dens_plot = dens_plot 
      }
      
      
      ggplotly(dens_plot)
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
        theme(axis.title = element_text(size = input$xylabelsize),
              title = element_text(size = input$titlesize),
              axis.text = element_text(size = input$xytextsize),
              legend.position = "none") 
      
      ggplotly(time_plot)
      
    } })
  })
 
  
  #output$plot_A = renderPlot({
  #  df_dens = df_draw()
  #  
  #  dens_plot = ggplot(df_dens, aes(x = value, y = muscle, fill = group,color = group)) + 
  #    geom_density_ridges( alpha = 0.5) + 
  #    facet_wrap(~ group, scales = "free_x")+
  #    theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
  #    theme(text = element_text(size = 20),
  #          legend.position = "none") 
    
  #  dens_plot
  #  dens_plot = ggplot(df_dens, aes(x = value, fill = group,color = group)) + 
  #    geom_density( alpha = 0.5) + 
  #    facet_wrap(~ group, scales = "free_x")+
  #    theme(panel.spacing.x = unit(0, "mm")) + theme_tufte()+
  #    theme(text = element_text(size = 20),
  #          legend.position = "none") 
    
  #  dens_plot
    
    
  # })
  
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
                    lengthMenu=list(c(10, -1), c('10', 'All'))), rownames= FALSE) %>%
      formatStyle(names(dt_table)[loc_value],
                  background = styleColorBar(rg, 'lightblue'),
                  backgroundSize = '98% 88%',
                  backgroundRepeat = 'no-repeat',
                  backgroundPosition = 'center')
    
  })
  
  
  output$DTtabletest1 <- DT::renderDataTable({
    dt_table = df_draw_test()
    if(dim(dt_table)[1]>0){
      dt_table = pivot_wider(dt_table, names_from = para)
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
  

  output$html1 <- renderUI({
    dt_test = df_draw_test()
    if(length(unique(dt_test$group))>=2){
    if (input$testselect1 == "Two sample t test"){
      dt_test = pivot_wider(dt_test, names_from = para)
      t.test.results <- nice_t_test(
      data = dt_test,
      response = input$testselect3,
      group = "group",
      warning = FALSE
    )
    t.test.results$d = NULL
    #t.test.results
    my_table <- nice_table(t.test.results)
    
    htmltools_value(my_table)
    } else if(input$testselect1 == "One-way ANOVA"){
      # anova one way
      res.aov = lm(value~group, dt_test)
      res.aov <- Anova(res.aov)
      HTML(kbl(res.aov)%>%
        kable_styling())
      
    }else if(input$testselect1 == "Tukey's HSD"){
      res.aov <- aov(value ~ group, data = dt_test)
      TK = TukeyHSD(res.aov)
      HTML(kbl((TK$group))%>%
             kable_styling())
    } 
      } else {
        HTML(
          "<font size= 50> Please fill in at least two groups to perform statistical tests </font>"
        )
      
    }
    
  })
  
}
