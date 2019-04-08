#!/bin/bash
set -xe

conda config --add channels conda-forge
conda config --add channels nsidc

conda install -y "conda-build=3.7.*"
conda install -y "anaconda-client=1.6.*"
