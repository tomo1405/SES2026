import pytest
from src_0321 import task_func

def test_task_func_with_valid_input():
    directory = "path/to/directory"
    file_list = ["file1.txt", "file2.txt"]
    expected_output = 0

    output = task_func(directory, file_list)

    assert output == expected_output

def test_task_func_with_invalid_input():
    directory = "path/to/directory"
    file_list = []
    expected_output = None

    output = task_func(directory, file_list)

    assert output == expected_output