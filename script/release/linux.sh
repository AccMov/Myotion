#!/bin/bash
cd ../../
# pack python package
pyinstaller main.py

# copy R script to dist folder
mkdir dist/main/shiny
cp shiny/*.R dist/main/shiny/

# copy logo
cp Myotion_logo.ico dist/main/Myotion_logo.ico

# should be removed
cp -r shiny/data dist/main/shiny/data

# install R from source
cd dist/main
wget http://cran.rstudio.com/src/base/R-3/R-3.6.3.tar.gz
tar xvf R-3.6.3.tar.gz
cd R-3.6.3
./configure --prefix=$PWD/../R
make && make install
