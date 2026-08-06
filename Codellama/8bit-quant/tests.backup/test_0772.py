import pytest
from src_0772 import task_func

def test_task_func():
    directory = 'path/to/directory'
    pattern = r'^(.*?)-\d+\.csv$'
    expected_new_files = ['file1.csv', 'file2.csv', 'file3.csv']

    new_files = task_func(directory, pattern)

    assert new_files == expected_new_files