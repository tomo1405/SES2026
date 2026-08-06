import pytest
from src_0509 import task_func

def test_task_func_valid_input():
    file_path1 = "path/to/file1"
    file_path2 = "path/to/file2"
    assert task_func(file_path1, file_path2) == True

def test_task_func_invalid_input():
    file_path1 = "path/to/file1"
    file_path2 = "path/to/file2"
    with pytest.raises(FileNotFoundError):
        task_func(file_path1, file_path2)