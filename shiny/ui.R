pacs = c("R.matlab","stringr","ggplot2","plotly","shinycssloaders",
          "ggthemes","shinydashboardPlus","DT","shiny","shinydashboard",
          "tidyverse","flextable","fresh","rempsyc","ggridges","shinyWidgets","XML")

lapply(pacs, require, character.only = TRUE)


# Define custom theme
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

# Convert Menu Item function
convertMenuItem <- function(mi, tabName) {
  mi$children[[1]]$attribs['data-toggle'] <- "tab"
  mi$children[[1]]$attribs['data-value'] <- tabName
  mi
}

# UI definition
ui <- dashboardPage(
  skin = "black",
  header = dashboardHeader(title = "Grouping"),
  sidebar = dashboardSidebar(
    sidebarMenu(id = "tab",
                menuItem("Data Visualizations", tabName = "groups", icon = icon("chart-bar")),
                menuItem("Statistical Tests", tabName = "tests", icon = icon("flask"))
    ),
    uiOutput("out1"),
    uiOutput("testtype")
  ),
  dashboardBody(
    # use_theme(accmovtheme), # Uncomment to use the theme
    tags$style(type = "text/css",
               ".shiny-output-error { visibility: hidden; }",
               ".shiny-output-error:before { visibility: hidden; }"
    ),
    tabItems(
      tabItem(tabName = "groups",
              fluidRow(
                box(
                  title = "Group A",
                  #pickerInput("filterA1", "Filter 1 (demo only)", choices = c("Male", "Female"), selected = "Male"),
                  uiOutput("filteruiA"),
                  collapsible = TRUE
                ),
                box(
                  title = "Group B",
                  #pickerInput("filterB1", "Filter 1 (demo only)", choices = c("Male", "Female"), selected = "Female"),
                  uiOutput("filteruiB"),
                  collapsible = TRUE
                ),
                tabBox(
                  height = 500, width = 12,
                  tabPanel("Figures",
                           uiOutput("uiplot1"),
                           DT::dataTableOutput("DTtable1") %>% withSpinner(color = "orange"))
                )
              )
      ),
      tabItem(tabName = "tests",
              fluidRow(
                lapply(1:6, function(i) {
                  box(
                    title = paste("Group", i),
                    pickerInput(paste0("filter", i, "1"), "Filter 1 (demo only)", choices = c("Male", "Female"), selected = "Female"),
                    uiOutput(paste0("filterui", i)),
                    collapsible = TRUE,
                    collapsed = TRUE
                  )
                }),
                tabBox(
                  height = 500, width = 12,
                  tabPanel("Statistical Tests",
                           htmlOutput("html1"),
                           DT::dataTableOutput("DTtabletest1") %>% withSpinner(color = "orange"))
                )
              )
      )
    )
  )
)




