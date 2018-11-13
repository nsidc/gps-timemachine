#!/bin/bash
set -xe

conda config --add channels conda-forge
conda config --add channels nsidc
conda config --add channels nsidc/label/dev

conda install -y "musher>=0.6.3,<1.0.0a"
conda install -y "conda-build <3.16.0" "anaconda-client=1.6.7"
