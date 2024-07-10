#!/bin/bash
cd ../../
# pack python package
pyinstaller main.py --noconfirm

# copy R script to dist folder
mkdir dist/main/shiny
cp shiny/*.R dist/main/shiny/

# copy logo
cp Myotion_logo.ico dist/main/Myotion_logo.ico

# should be removed
cp -r shiny/data dist/main/shiny/data

# install R from source, compatible with all dist
cd dist/main
wget http://cran.rstudio.com/src/base/R-3/R-4.3.2.tar.gz
tar xvf R-4.3.2.tar.gz
cd R-4.3.2
./configure --prefix=$PWD/../R
make && make install
