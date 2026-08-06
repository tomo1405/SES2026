import glob


def calculate_assertion_rate(log_dir):
    passed = failed = errored = 0

    for log_file in glob.glob(f"{log_dir}/*.log"):
        with open(log_file) as f:
            first_line = f.readline()

        passed += first_line.count(".")
        failed += first_line.count("F")
        errored += first_line.count("E")

    total = passed + failed + errored
    return (passed / total * 100) if total else 0


def save_assertion_rate(log_dir, rate):
    with open(f"{log_dir}_AssertionRate.txt", "w") as f:
        f.write(f"{rate:.2f}%")


def main():
    for log_dir in ("C0_logs", "C1_logs"):
        rate = calculate_assertion_rate(log_dir)
        save_assertion_rate(log_dir, rate)

    print("完了しました")


if __name__ == "__main__":
    main()