cd ../../
# pack python package
pyinstaller main.py

# copy R script to dist folder
mkdir dist/main/shiny
xcopy /s "shiny\*.R" "dist\main\shiny\*.R"

# copy logo
xcopy /s "Myotion_logo.ico" "dist\main\Myotion_logo.ico"

# should be removed
xcopy /s "shiny\data" "dist\main\shiny\data"