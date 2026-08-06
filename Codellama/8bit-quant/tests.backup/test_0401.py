import pytest
from src_0401 import task_func

def test_task_func():
    directory = "path/to/directory"
    string = "string"
    expected_files = ["path/to/file1.json", "path/to/file2.json"]

    found_files = task_func(directory, string)

    assert found_files == expected_files