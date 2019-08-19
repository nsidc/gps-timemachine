#!/bin/bash
set -xe

conda config --add channels conda-forge
conda config --add channels nsidc
conda config --set anaconda_upload no

conda install -y "conda-build=3.17" "anaconda-client=1.7" "conda-verify"
