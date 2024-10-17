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

:: checkout R-win-4.3.4 to dist
mkdir "dist\main\R"
git clone -b R-4.3.4 https://github.com/X-Motion/R.git "dist\main\R"