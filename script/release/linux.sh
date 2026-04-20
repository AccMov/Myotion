#!/bin/bash
# pack python package
pyinstaller main.py --noconfirm --noconsole --distpath "dist" --workpath "build" -n Myotion

# copy R script to dist folder
mkdir dist/Myotion/shiny
cp shiny/*.R dist/Myotion/shiny/
cp shiny/translations_from_csv.json dist/Myotion/shiny/

# copy logo
cp Myotion_logo.ico dist/Myotion/Myotion_logo.ico

# install R from source, compatible with all dist
# this is not tested
cd dist/Myotion
wget http://cran.rstudio.com/src/base/R-3/R-4.3.4.tar.gz
tar xvf R-4.3.4.tar.gz
cd R-4.3.4
./configure --prefix=$PWD/../R
make && make install
