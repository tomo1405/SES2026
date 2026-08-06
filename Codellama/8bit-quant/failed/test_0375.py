import pytest
from src_0375 import task_func

def test_task_func_valid_directory():
    directory_path = './xlsx_files/'
    processed_files = task_func(directory_path)
    assert processed_files == 2

def test_task_func_invalid_directory():
    directory_path = './invalid_directory/'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)