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
        (
            "/home/user/Documents",
            "/",
            [
                ("home", {"total": 100000000000, "used": 2000000000, "free": 80000000000}),
                ("user", {"total": 100000000000, "used": 1500000000, "free": 85000000000}),
                ("Documents", {"total": 100000000000, "used": 500000000, "free": 95000000000}),
            ],
        ),
        (
            "C:/Users/John/Pictures",
            "\\",
            [
                ("C:", {"total": 100000000000, "used": 2000000000, "free": 80000000000}),
                ("Users", {"total": 100000000000, "used": 1500000000, "free": 85000000000}),
                ("John", {"total": 100000000000, "used": 500000000, "free": 95000000000}),
                ("Pictures", {"total": 100000000000, "used": 200000000, "free": 98000000000}),
            ],
        ),
    ]

    for test_case in test_cases:
        path, delimiter, expected_output = test_case
        with pytest.raises(Exception) as exc_info:
            task_func(path, delimiter)
        assert str(exc_info.value) == "Path must be a non-empty string"