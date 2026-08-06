import pytest
from src_1110 import task_func

def test_task_func():
    file_path = 'File.txt'
    tokens = task_func(file_path)
    assert tokens == ['token1', 'token2', 'token3']

def test_task_func_invalid_file():
    file_path = 'Invalid.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)