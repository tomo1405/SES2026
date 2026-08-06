import pytest
from src_0375 import task_func

def test_task_func():
    # Test case 1: directory_path is a valid directory
    processed_files = task_func('./xlsx_files/')
    assert processed_files > 0

    # Test case 2: directory_path is not a valid directory
    with pytest.raises(FileNotFoundError):
        task_func('invalid_directory_path')

    # Test case 3: directory_path is a file
    with pytest.raises(FileNotFoundError):
        task_func('test.txt')