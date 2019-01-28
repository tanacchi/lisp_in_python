#! /bin/bash

python_dir=$(cd $(dirname ${BASH_SOURCE}); pwd)/../

python3 -m unittest discover ${python_dir}/tests
