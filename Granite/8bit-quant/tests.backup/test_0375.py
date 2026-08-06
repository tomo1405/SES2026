import pytest
from src_0375 import task_func

def test_task_func():
    # Test case 1: directory_path is a valid directory
    directory_path = './xlsx_files/'
    processed_files = task_func(directory_path)
    assert processed_files > 0

    # Test case 2: directory_path is not a valid directory
    directory_path = '/invalid_directory/'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)