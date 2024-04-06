require(shiny)

# get path of current script
initial.options <- commandArgs(trailingOnly = FALSE)
file.arg.name <- "--file="
script.name <- sub(file.arg.name, "", initial.options[grep(file.arg.name, initial.options)])
script.dirname <- dirname(script.name)
setwd(script.dirname)

source('server.R', local = TRUE)
source('ui.R', local = TRUE)

shinyApp(ui = ui, server = server)

