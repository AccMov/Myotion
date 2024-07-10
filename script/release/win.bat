cd ../../
:: pack python package
pyinstaller main.py --noconfirm

:: copy R script to dist folder
mkdir "dist/main/shiny"
xcopy /s "shiny\*.R" "dist\main\shiny\*.R"

:: copy logo
xcopy /s "Myotion_logo.ico" "dist\main\Myotion_logo.ico"

:: should be removed
mkdir "dist\main\shiny\data"
xcopy /s "shiny\data\*" "dist\main\shiny\data\"

:: copy R-4.3.4 to dist
mkdir "dist\main\R"
xcopy /s "R" "dist\main\R"