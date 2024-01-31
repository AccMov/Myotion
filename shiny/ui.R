library(R.matlab)
library(stringr)
library(ggplot2)
library(plotly)
library(DT)
#library(bslib)
library(shinydashboardPlus)
library(ggthemes)
library(shinycssloaders)
library(shiny)
library(shinydashboard)
library(tidyverse)
library(ggridges)
library(shinyWidgets)
library(fresh)

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

accmovtheme <- create_theme(
  bs4dash_vars(
    navbar_light_color = "#bec5cb",
    navbar_light_active_color = "#FFF",
    navbar_light_hover_color = "#FFF"
  ),
  bs4dash_yiq(
    contrasted_threshold = 10, 
    text_dark = "#FFF", 
    text_light = "#272c30"
  ),
  bs4dash_layout(main_bg = "#353c42"),
  bs4dash_sidebar_dark(
    bg = "#272c30", 
    color = "#bec5cb", 
    hover_color = "#FFF",
    submenu_bg = "#272c30", 
    submenu_color = "#FFF", 
    submenu_hover_color = "#FFF"
  ),
  bs4dash_status(dark = "#272c30"),
  bs4dash_color(gray_900 = "#FFF", white = "#272c30")
)

convertMenuItem <- function(mi,tabName) {
  mi$children[[1]]$attribs['data-toggle']="tab"
  mi$children[[1]]$attribs['data-value'] = tabName
  mi
}

ui <- dashboardPage(  skin = "black",
                     dashboardHeader(title = "Grouping"),
                     
                     dashboardSidebar( 
                       sidebarMenu(

                         menuItem("Compare groups", tabName = "groups", icon = icon("gro")), # No icon yet
                         selectInput("select1", "Select domain ", choices = domain,
                                     selected = "time_domain_para"),
                         uiOutput('uiselect1'),
                         uiOutput('uiselect2'),
                         uiOutput('uiselect3'),
                         menuItem("Figure options", tabName = "figop", icon = icon("pltop"),
                                  uiOutput("plotoption")),
                         menuItem("Hypothesis test options", tabName = "hypotest", icon = icon("hypo"),
                                  pickerInput("hypotest1", "Inference for", choices = c("Group A", "Group B", "Comparing Group A & Group B"),
                                              selected = "Group A"),
                                  uiOutput('uiselect4'),
                                  uiOutput('uihypotest1'),
                                  radioButtons(
                                    inputId = "hypotest2",
                                    label = "Alternative Hypothesis",
                                    choices = c(
                                      "\\( \\neq \\)" = "two.sided",
                                      "\\( > \\)" = "greater",
                                      "\\( < \\)" = "less"
                                    )),
                                  sliderInput("hypotest3",
                                              "Significance level \\(\\alpha = \\)",
                                              min = 0.01,
                                              max = 0.20,
                                              value = 0.05
                                  )
                         )
                         
                         

                       )
                      
                     ),
                     dashboardBody(
                        #use_theme(accmovtheme),
                                   tags$style(type="text/css",
                                              ".shiny-output-error { visibility: hidden; }",
                                              ".shiny-output-error:before { visibility: hidden; }"
                                   ),
                                   tabItems(
                       # First tab content
                       tabItem(tabName = "groups",
                               fluidRow(
                                 box(title = "Group A",
                                     pickerInput("filterA1", "Filter 1 (demo only)", choices = c("Male","Female"),
                                                 selected = "Male"),
                                     pickerInput("filterA2", "Add by ID", choices = c(names(groupA)),
                                                 selected = c("Results.GA.PP001","Results.GA.PP002","Results.GA.PP003","Results.GA.PP004",
                                                              "Results.GA.PP005","Results.GA.PP006","Results.GA.PP007","Results.GA.PP008"),
                                                 multiple = TRUE),
                                     collapsible = TRUE),
                                 
                                 box(
                                   title = "Group B",
                                   pickerInput("filterB1", "Filter 1 (demo only)", choices = c("Male","Female"),
                                               selected = "Female"),
                                   pickerInput("filterB2", "Add by ID", choices = c(names(groupB)),
                                               selected = c("Results.GB.PP001","Results.GB.PP002","Results.GB.PP003","Results.GB.PP004",
                                                            "Results.GB.PP005","Results.GB.PP006","Results.GB.PP007","Results.GB.PP008","Results.GB.PP009"),
                                               multiple = TRUE),
                                   collapsible = TRUE
                                 ),
                                 tabBox(height = 500,width = 12,
                                     tabPanel("Figures",
                                       uiOutput("uiplot1")),
                                     tabPanel("Data table",
                                              DT::dataTableOutput("DTtable1")%>% withSpinner(color="orange")
                                              ),
                                     tabPanel("Hypothesis test",
                                              "Filtered data:",
                                              DT::dataTableOutput("testdata"),
                                              uiOutput("testtext"),
                                              plotOutput("testplot")
                                     )
                                     )
                                 
                               )
                       ),
                       
                       # Second tab content
                       tabItem(tabName = "individuals",
                               h2("Nothing yet")
                       )
                     )
                     )           )

