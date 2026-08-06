import pytest
from src_0509 import task_func

def test_task_func_valid_filepaths():
    file_path1 = "path/to/file1.txt"
    file_path2 = "path/to/file2.txt"
    assert task_func(file_path1, file_path2) == True

def test_task_func_invalid_filepaths():
    file_path1 = "path/to/file1.txt"
    file_path2 = "path/to/file2.txt"
    with pytest.raises(FileNotFoundError):
        task_func(file_path1, file_path2)