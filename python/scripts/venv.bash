#! /bin/bash

python_dir=$(cd $(dirname ${BASH_SOURCE}); pwd)/../

if [ ! -f "${python_dir}/venv/bin/activate" ]; then
  python3 -m virtualenv venv/
fi

source ${python_dir}/venv/bin/activate
