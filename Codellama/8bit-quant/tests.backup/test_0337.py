import pytest
from src_0337 import task_func

def test_task_func():
    pattern = "hello"
    directory = "tests/test_data"
    extensions = ["*.txt", "*.py"]
    expected_files = [
        "tests/test_data/hello.txt",
        "tests/test_data/hello.py"
    ]
    actual_files = task_func(pattern, directory, extensions)
    assert actual_files == expected_files