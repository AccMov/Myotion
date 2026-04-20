:: pack python package
pyinstaller main.py --noconfirm --noconsole --distpath "dist" --workpath "build" -n Myotion

:: copy R script to dist folder
mkdir "dist/Myotion/shiny"
xcopy /s "shiny\*.R" "dist\Myotion\shiny\*.R"
copy "shiny\translations_from_csv.json" "dist\Myotion\shiny\translations_from_csv.json"

:: copy logo 
copy "Myotion_logo.ico" "dist\Myotion\Myotion_logo.ico"

:: checkout R-win-4.3.4 to dist
mkdir "dist\Myotion\R"
git clone -b R-4.3.4 https://github.com/X-Motion/R.git "dist\Myotion\R"