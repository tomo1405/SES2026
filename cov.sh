#!/bin/bash

cd /work/tomohiro-w/utg/Qwen/non-quant/tests || exit 1

mkdir -p passed failed

for test_file in ./test_*.py
do
    filename=$(basename "$test_file")
    src_file="../../src/${filename/test_/src_}"

    # 対応するソースがない場合
    if [ ! -f "$src_file" ]; then
        cp "$test_file" failed/
        continue
    fi

    coverage erase

    if coverage run --source=../../src -m pytest "$test_file" > /dev/null 2>&1
    then
        cp "$test_file" passed/
    else
        cp "$test_file" failed/
    fi
done