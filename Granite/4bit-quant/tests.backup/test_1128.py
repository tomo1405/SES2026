import os
import re
import hashlib
import pytest

def task_func(path, delimiter):
    path_components = re.split(f'({delimiter})', path)
    hashes = []

    for component in path_components:
        if not component:  # Remove empty components
            continue
        if component != delimiter and os.path.isfile(component):
            with open(component, 'rb') as f:
                hashes.append(hashlib.sha256(f.read()).hexdigest())
        else:
            hashes.append(None)

    return list(zip(path_components, hashes))

def test_task_func():
    test_cases = [
        (
            "path/to/file1.txt",
            ".",
            [("path", None), ("to", None), ("file1.txt", "5e4b6365d102c64690361a2c059c2d5230619d5e021b599e7f4902092231e00e")]
        ),
        (
            "path/to/file2.txt.gz",
            ".",
            [("path", None), ("to", None), ("file2.txt", "5e4b6365d102c64690361a2c059c2d5230619d5e021b599e7f4902092231e00e"), ("gz", None)]
        ),
        (
            "path/to/dir1/",
            "/",
            [("path", None), ("to", None), ("dir1", None), ("", None)]
        ),
        (
            "path/to/dir2/",
            "/",
            [("path", None), ("to", None), ("dir2", None), ("", None)]
        ),
    ]

    for test_case in test_cases:
        path, delimiter, expected_output = test_case
        actual_output = task_func(path, delimiter)
        assert actual_output == expected_output, f"Failed for input: {path}, {delimiter}"

if __name__ == "__main__":
    pytest.main()