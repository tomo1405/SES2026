#!/bin/bash

test_dirs=(
    "/work/tomohiro-w/utg/Qwen/non-quant/tests"
    "/work/tomohiro-w/utg/Qwen/4bit-quant/tests"
    "/work/tomohiro-w/utg/Qwen/8bit-quant/tests"
    "/work/tomohiro-w/utg/Granite/non-quant/tests"
    "/work/tomohiro-w/utg/Granite/4bit-quant/tests"
    "/work/tomohiro-w/utg/Granite/8bit-quant/tests"
    "/work/tomohiro-w/utg/Codellama/non-quant/tests"
    "/work/tomohiro-w/utg/Codellama/4bit-quant/tests"
    "/work/tomohiro-w/utg/Codellama/8bit-quant/tests"
)

max_retry=5
max_time=300
pytest_timeout=120

# NameError のエイリアス補完
declare -A aliases=(
    [np]="import numpy as np"
    [pd]="import pandas as pd"
    [plt]="import matplotlib.pyplot as plt"
    [sns]="import seaborn as sns"
    [tf]="import tensorflow as tf"
    [torch]="import torch"
)

for test_dir in "${test_dirs[@]}"
do
    echo
    echo "========================================"
    echo "Directory: $test_dir"
    echo "========================================"

    backup_dir="${test_dir}.backup"

    if [ ! -d "$backup_dir" ]; then
        echo "Creating backup: $backup_dir"
        cp -a "$test_dir" "$backup_dir"
    else
        echo "Backup already exists: $backup_dir"
    fi

    cd "$test_dir" || {
        echo "Cannot enter $test_dir"
        continue
    }

    for test_file in test_*.py
    do
        [ -f "$test_file" ] || continue

        echo
        echo "=== Testing $test_file ==="

        retry=0
        start_time=$(date +%s)

        while true
        do
            now=$(date +%s)

            if (( now - start_time >= max_time )); then
                echo "Timeout (${max_time}s)"
                break
            fi

            output=$(timeout "$pytest_timeout" \
                coverage run -m pytest --tb=long "$test_file" 2>&1)
            status=$?

            if (( status == 124 )); then
                echo "pytest timed out (${pytest_timeout}s)"
                break
            fi

            if ! grep -q "NameError" <<<"$output"; then
                echo "done"
                break
            fi

            ((retry++))

            if (( retry > max_retry )); then
                echo "Reached max retry ($max_retry)"
                echo "$output"
                break
            fi

            before=$(sha256sum "$test_file" | cut -d' ' -f1)

            # NameError の識別子を取得
            name=$(echo "$output" |
                sed -n "s/.*NameError: name '\([^']*\)' is not defined.*/\1/p" |
                head -1)

            # エイリアスなら import を追加
            if [[ -n "$name" && -n "${aliases[$name]}" ]]; then
                import_stmt="${aliases[$name]}"

                if ! grep -Fxq "$import_stmt" "$test_file"; then
                    echo "Adding alias import: $import_stmt"

                    tmp=$(mktemp)
                    {
                        echo "$import_stmt"
                        cat "$test_file"
                    } > "$tmp"
                    mv "$tmp" "$test_file"
                fi
            fi

            autoimport "$test_file"
            isort "$test_file"

            after=$(sha256sum "$test_file" | cut -d' ' -f1)

            if [ "$before" = "$after" ]; then
                echo "autoimport made no changes."
                echo "$output"
                break
            fi
        done
    done
done

echo
echo "All directories processed."