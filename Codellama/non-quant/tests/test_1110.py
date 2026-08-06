import pytest
from src_1110 import task_func

def test_task_func_valid_file():
    file_path = 'File.txt'
    tokens = task_func(file_path)
    assert tokens == ['Hello', 'world!']

def test_task_func_invalid_file():
    file_path = 'Invalid.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)