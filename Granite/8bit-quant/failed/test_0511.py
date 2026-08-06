import pytest
from src_0511 import task_func

def test_task_func():
    file_path1 = 'path/to/file1.txt.gz'
    file_path2 = 'path/to/file2.txt.gz'
    expected_output = 'This is the expected output of the function'

    actual_output = task_func(file_path1, file_path2)

    assert actual_output == expected_output