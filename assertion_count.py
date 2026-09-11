from pathlib import Path


SES2026_DIR = Path(__file__).resolve().parent
MODELS = ("Codellama", "Qwen", "Granite")
QUANTIZATIONS = ("non-quant", "4bit-quant", "8bit-quant")
LOG_DIRS = ("C0_logs", "C1_logs")


def count_assertion_number(log_dir):
    passed = failed = errored = 0
    files = sorted(log_dir.glob("*.log"))

    for log_file in files:
        with log_file.open(encoding="utf-8") as f:
            first_line = f.readline()

        passed += first_line.count(".")
        failed += first_line.count("F")
        errored += first_line.count("E")

    return passed + failed + errored, len(files)


def save_data(tests_dir, log_dir_name, count):
    output_file = tests_dir / f"{log_dir_name}_AssertionCount.txt"
    output_file.write_text(str(count), encoding="utf-8")


def process_tests_dir(model, quantization):
    tests_dir = SES2026_DIR / model / quantization / "tests"

    if not tests_dir.is_dir():
        print(f"[スキップ] {model}/{quantization}: testsフォルダーがありません")
        return

    for log_dir_name in LOG_DIRS:
        log_dir = tests_dir / log_dir_name
        if not log_dir.is_dir():
            print(f"[スキップ] {model}/{quantization}/{log_dir_name}: フォルダーがありません")
            continue

        count, file_count = count_assertion_number(log_dir)
        save_data(tests_dir, log_dir_name, count)
        print(
            f"{model}/{quantization}/{log_dir_name}: "
            f"ログ{file_count}件、アサーション結果{count}件"
        )


def main():
    for model in MODELS:
        for quantization in QUANTIZATIONS:
            process_tests_dir(model, quantization)

    print("完了しました")


if __name__ == "__main__":
    main()
