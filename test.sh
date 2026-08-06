#!/bin/bash

cd /work/tomohiro-w/utg/Qwen/non-quant/tests || exit 1

touch requirements.txt

for test_file in ./test_*.py
do
    filename=$(basename "$test_file")
    src_file="../../src/${filename/test_/src_}"

    coverage run -m pytest $filename
done