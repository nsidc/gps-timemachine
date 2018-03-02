#!/bin/bash
set -xe

conda config --add channels conda-forge
conda config --add channels nsidc
conda config --add channels nsidc/label/dev

conda install -y "musher>=0.6.3,<0.7.0"
conda install -y invoke=0.13.0 conda-build anaconda-client
