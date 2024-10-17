require(shiny)
require(shiny.i18n)

# get path of current script
initial.options <- commandArgs(trailingOnly = FALSE)
file.arg.name <- "--file="
script.name <- sub(file.arg.name, "", initial.options[grep(file.arg.name, initial.options)])
script.dirname <- dirname(script.name)
setwd(script.dirname)

language.arg.name <- "--language="
lan.name <- sub(language.arg.name, "", initial.options[grep(language.arg.name, initial.options)])


i18n <- Translator$new(translation_json_path='translations_from_csv.json')
i18n$set_translation_language(lan.name)

source('ui.R', local = TRUE)
source('server.R', local = TRUE)

shinyApp(ui = ui, server = server)

