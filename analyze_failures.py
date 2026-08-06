import subprocess
import sys
import re
import os
import json
from collections import Counter, defaultdict

VARIANT = sys.argv[1]
BASE = f"/work/tomohiro-w/utg/Codellama/{VARIANT}"
FAILED_DIR = f"{BASE}/failed"
SRC_DIR = "/work/tomohiro-w/utg/src"

SUMMARY_LINE = re.compile(r"^(FAILED|ERROR) (\S+)", re.MULTILINE)
E_LINE = re.compile(r"^E\s+(.*)$", re.MULTILINE)
EXC_NAME = re.compile(r"^([\w.]*?(?:Error|Exception|Warning))\b")

def categorize_message(msg):
    msg = msg.strip()
    m = EXC_NAME.match(msg)
    if m:
        return m.group(1)
    if msg.startswith("assert"):
        return "AssertionError"
    if msg.startswith("Failed:"):
        return "pytest.fail"
    first_word = msg.split(":")[0].split()[0] if msg else "EMPTY"
    return f"OTHER({first_word})"

def classify(filename):
    src_name = filename.replace("test_", "src_")
    src_path = os.path.join(SRC_DIR, src_name)
    if not os.path.isfile(src_path):
        return "NO_SRC_FILE", None

    test_path = os.path.join(FAILED_DIR, filename)
    try:
        proc = subprocess.run(
            ["/work/tomohiro-w/utg/.venv/bin/python", "-m", "pytest", test_path, "--tb=line", "-q"],
            cwd=BASE,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT", None

    out = proc.stdout + proc.stderr

    if "ERROR collecting" in out or "errors during collection" in out or "ImportError while importing test module" in out:
        m = re.search(r"^E\s+(\w+(?:Error|Exception)):", out, re.MULTILINE)
        if m:
            return f"COLLECTION_{m.group(1)}", out[-1500:]
        return "COLLECTION_ERROR_OTHER", out[-1500:]

    summary_matches = SUMMARY_LINE.findall(out)
    e_matches = E_LINE.findall(out)
    if summary_matches:
        kind, _node = summary_matches[0]
        prefix = "ERROR_" if kind == "ERROR" else ""
        msg = e_matches[-1] if e_matches else ""
        return f"{prefix}{categorize_message(msg)}", out[-1500:]

    if proc.returncode == 0:
        return "ACTUALLY_PASSES_NOW", out[-500:]

    return "UNKNOWN", out[-1500:]

def main():
    files = sorted(f for f in os.listdir(FAILED_DIR) if f.endswith(".py"))
    counter = Counter()
    examples = defaultdict(list)

    for i, filename in enumerate(files, 1):
        category, detail = classify(filename)
        counter[category] += 1
        if len(examples[category]) < 3:
            examples[category].append({"file": filename, "detail": detail})
        if i % 100 == 0:
            print(f"[{VARIANT}] {i} / {len(files)}", flush=True)

    result = {
        "variant": VARIANT,
        "total": len(files),
        "counts": counter.most_common(),
        "examples": examples,
    }
    out_path = f"/work/tomohiro-w/utg/Codellama/{VARIANT}/failure_analysis.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"[{VARIANT}] wrote {out_path}")
    for cat, cnt in counter.most_common():
        print(f"  {cat}: {cnt}")

if __name__ == "__main__":
    main()
