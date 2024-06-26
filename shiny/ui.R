pacs = c("R.matlab","stringr","ggplot2","plotly","shinycssloaders",
          "ggthemes","shinydashboardPlus","DT","shiny","shinydashboard",
          "tidyverse","flextable","fresh","rempsyc","ggridges","shinyWidgets","XML")

lapply(pacs, require, character.only = TRUE)


groupA_names <- list.files("data/Group_A", pattern="*.xml", full.names=TRUE)
groupA <- lapply(groupA_names, xmlToList)

for(i in 1:length(groupA)){
  names(groupA)[i] = groupA[[i]]$Person$name
}


# Time domain parameters names
time_domain_para = names(groupA$ABC1$emg$statistic)[1:13]
freq_domain_para = names(groupA$ABC1$emg$statistic)[14:20]
advanced = names(groupA$ABC1$emg$timeSeriesTable$channels)

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
                                          header = dashboardHeader(title = "Grouping"),
                                          
                                          

                                          
                     sidebar = dashboardSidebar( 
                       
                       sidebarMenu(id = "tab", 
                                   
                                   menuItem("Data visulizations", tabName = "groups", icon = icon("gro")), # No icon yet
                                   menuItem("Statistical tests", tabName = "tests", icon = icon("tst")) # No icon yet
                                   
                       ),
                       uiOutput("out1"),
                       uiOutput("testtype")
                       
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
                                                 selected = c("ABC1","ABC2","ABC3","ABC4"),
                                                 multiple = TRUE),
                                     collapsible = TRUE),
                                 
                                 box(
                                   title = "Group B",
                                   pickerInput("filterB1", "Filter 1 (demo only)", choices = c("Male","Female"),
                                               selected = "Female"),
                                   pickerInput("filterB2", "Add by ID", choices = c(names(groupA)),
                                               selected = c("ABC1","ABC2","ABC3","ABC4"),
                                               multiple = TRUE),
                                   collapsible = TRUE
                                 ),
                                 tabBox(
                                   height = 500,width = 12,
                                     tabPanel("Figures",
                                       uiOutput("uiplot1"),
                                       DT::dataTableOutput("DTtable1")%>% withSpinner(color="orange"))
                                     )
                                 
                               )
                       ),
                       
                       # Second tab content
                       tabItem(tabName = "tests",
                               fluidRow(
                                 box(title = "Group 1",
                                     pickerInput("filter11", "Filter 1 (demo only)", choices = c("Male","Female"),
                                                 selected = "Male"),
                                     pickerInput("filter12", "Add by ID", choices = c(names(groupA)),
                                                 selected = NULL,
                                                 multiple = TRUE),
                                     collapsible = TRUE,
                                     collapsed = T),
                                 box(
                                   title = "Group 2",
                                   pickerInput("filter21", "Filter 1 (demo only)", choices = c("Male","Female"),
                                               selected = "Female"),
                                   pickerInput("filter22", "Add by ID", choices = c(names(groupA)),
                                               selected = NULL,
                                               multiple = TRUE),
                                   collapsible = TRUE,
                                   collapsed = T
                                 ),
                                 box(
                                   title = "Group 3",
                                   pickerInput("filter31", "Filter 1 (demo only)", choices = c("Male","Female"),
                                               selected = "Female"),
                                   pickerInput("filter32", "Add by ID", choices = c(names(groupA)),
                                               selected = NULL,
                                               multiple = TRUE),
                                   collapsible = TRUE,
                                   collapsed = T
                                 ),
                                 box(
                                   title = "Group 4",
                                   pickerInput("filter41", "Filter 1 (demo only)", choices = c("Male","Female"),
                                               selected = "Female"),
                                   pickerInput("filter42", "Add by ID", choices = c(names(groupA)),
                                               selected = NULL,
                                               multiple = TRUE),
                                   collapsible = TRUE,
                                   collapsed = T
                                 ),
                                 box(
                                   title = "Group 5",
                                   pickerInput("filter51", "Filter 1 (demo only)", choices = c("Male","Female"),
                                               selected = "Female"),
                                   pickerInput("filter52", "Add by ID", choices = c(names(groupA)),
                                               selected = NULL,
                                               multiple = TRUE),
                                   collapsible = TRUE,
                                   collapsed = T
                                 ),
                                 box(
                                   title = "Group 6",
                                   pickerInput("filter61", "Filter 1 (demo only)", choices = c("Male","Female"),
                                               selected = "Female"),
                                   pickerInput("filter62", "Add by ID", choices = c(names(groupA)),
                                               selected = NULL,
                                               multiple = TRUE),
                                   collapsible = TRUE,
                                   collapsed = T
                                 ),
                                 tabBox(
                                        height = 500,width = 12,
                                        tabPanel("Statistical tests",
                                                 htmlOutput("html1"),
                                                 DT::dataTableOutput("DTtabletest1")%>% withSpinner(color="orange"))
                                 )
                                 
                               )
                       )
                     )
                     )           )





