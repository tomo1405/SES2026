import pytest
from src_0155 import task_func

def test_task_func():
    directory = 'path/to/directory'
    file_pattern = '*.txt'
    suffix = '.txt'
    expected_file_types = {'file1.txt': 'text/plain', 'file2.txt': 'text/plain'}

    file_types = task_func(directory, file_pattern, suffix)

    assert file_types == expected_file_types