#!/bin/bash
# 1テストファイルずつ独立したプロセス・独立したcoverageデータで計測するスクリプト。
# test_dirs に列挙した全ディレクトリに対して順に実行する。
# 使い方: ./cov_accurate.sh

set -uo pipefail

test_dirs=(
    # "/work/tomohiro-w/utg/Qwen/non-quant/tests"
    # "/work/tomohiro-w/utg/Qwen/4bit-quant/tests"
    # "/work/tomohiro-w/utg/Qwen/8bit-quant/tests"
    # "/work/tomohiro-w/utg/Granite/non-quant/tests"
    "/work/tomohiro-w/utg/Granite/4bit-quant/tests"
    # "/work/tomohiro-w/utg/Granite/8bit-quant/tests"
    # "/work/tomohiro-w/utg/Codellama/non-quant/tests"
    # "/work/tomohiro-w/utg/Codellama/4bit-quant/tests"
    # "/work/tomohiro-w/utg/Codellama/8bit-quant/tests"
)

SRC_DIR="../../../src"
TIMEOUT_SEC=120

run_dir() {
    local test_dir="$1"

    echo
    echo "========================================"
    echo "Directory: $test_dir"
    echo "========================================"

    if [ ! -d "$test_dir" ]; then
        echo "Cannot find $test_dir, skipping"
        return
    fi

    (
        cd "$test_dir" || exit 1
        LOG_DIR="./C0_logs"
        mkdir -p "$LOG_DIR"
        RESULTS_CSV="./coverage_results_C0.csv"
        COMBINED_COVERAGE_FILE="./.coverage_C0"
        echo "test_file,src_file,status,percent" > "$RESULTS_CSV"

        count=0
        total=$(ls ./test_*.py 2>/dev/null | wc -l)

        for test_file in ./test_*.py
        do
            count=$((count + 1))
            filename=$(basename "$test_file")
            src_file="${SRC_DIR}/${filename/test_/src_}"

            if [ ! -f "$src_file" ]; then
                echo "${filename},,no_src," >> "$RESULTS_CSV"
                continue
            fi

            data_file=".coverage.${filename}_C0"
            rm -f "$data_file"

            COVERAGE_FILE="$data_file" timeout "$TIMEOUT_SEC" \
                coverage run --include="$src_file" -m pytest -q "$test_file" \
                > "${LOG_DIR}/${filename}.log" 2>&1
            status=$?

            if [ "$status" -eq 124 ]; then
                echo "${filename},$(basename "$src_file"),timeout," >> "$RESULTS_CSV"
                continue
            fi

            percent=$(COVERAGE_FILE="$data_file" coverage report 2>/dev/null | tail -1 | awk '{print $NF}')

            if [ -z "$percent" ]; then
                echo "${filename},$(basename "$src_file"),no_coverage_data," >> "$RESULTS_CSV"
            else
                echo "${filename},$(basename "$src_file"),done,${percent}" >> "$RESULTS_CSV"
            fi

            if [ $((count % 50)) -eq 0 ]; then
                echo "[$test_dir] $count / $total done"
            fi
        done

        echo "Combining per-file coverage data into one browsable report..."
        rm -f "$COMBINED_COVERAGE_FILE"
        COVERAGE_FILE="$COMBINED_COVERAGE_FILE" coverage combine .coverage.test_*.py_C0 2>/dev/null
        COVERAGE_FILE="$COMBINED_COVERAGE_FILE" coverage html -d htmlcov_accurate_C0

        echo "Done. See ${test_dir}/coverage_results_C0.csv and ${test_dir}/htmlcov_accurate_C0/index.html"
    )
}

for test_dir in "${test_dirs[@]}"
do
    echo "$test_dir"
    run_dir "$test_dir"
done

echo
echo "All directories processed."
