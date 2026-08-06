import pytest
from src_0722 import task_func

def test_task_func():
    file_path = 'path/to/your/file.csv'
    expected_output = ('the', 10)

    actual_output = task_func(file_path)

    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_file_path():
    file_path = 'path/to/your/invalid/file.csv'
    expected_output = None

    actual_output = task_func(file_path)

    assert actual_output == expected_output, "Output does not match expected output"