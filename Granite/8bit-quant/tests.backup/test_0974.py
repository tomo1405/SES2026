import os
import shutil
import pytest

def task_func(path, delimiter="/"):
    if not path or not isinstance(path, str):
        raise ValueError("Path must be a non-empty string")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist")

    path_components = path.strip(delimiter).split(delimiter)
    if not all(path_components):
        raise ValueError("Path contains invalid components")

    results = []
    for index, component in enumerate(path_components):
        sub_path = delimiter.join(path_components[: index + 1])
        if not sub_path.startswith(delimiter):
            sub_path = delimiter + sub_path
        usage = shutil.disk_usage(sub_path)
        results.append(
            (component, {"total": usage.total, "used": usage.used, "free": usage.free})
        )

    return results

def test_task_func():
    test_cases = [
        {
            "path": "/home/user/Documents",
            "delimiter": "/",
            "expected_output": [
                ("home", {"total": 100000000000, "used": 50000000000, "free": 50000000000}),
                ("user", {"total": 100000000000, "used": 25000000000, "free": 75000000000}),
                ("Documents", {"total": 100000000000, "used": 10000000000, "free": 90000000000}),
            ],
        },
        {
            "path": "C:/Users/John/Documents",
            "delimiter": "\\",
            "expected_output": [
                ("C:", {"total": 100000000000, "used": 50000000000, "free": 50000000000}),
                ("Users", {"total": 100000000000, "used": 25000000000, "free": 75000000000}),
                ("John", {"total": 100000000000, "used": 10000000000, "free": 90000000000}),
                ("Documents", {"total": 100000000000, "used": 5000000000, "free": 95000000000}),
            ],
        },
    ]

    for test_case in test_cases:
        path = test_case["path"]
        delimiter = test_case["delimiter"]
        expected_output = test_case["expected_output"]

        actual_output = task_func(path, delimiter)

        assert actual_output == expected_output, f"Test failed for path '{path}' and delimiter '{delimiter}'"

if __name__ == "__main__":
    pytest.main()