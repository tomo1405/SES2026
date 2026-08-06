import pytest
from src_1110 import task_func

def test_task_func():
    file_path = 'File.txt'
    tokens = task_func(file_path)
    assert isinstance(tokens, list)
    assert all(isinstance(token, str) for token in tokens)

def test_task_func_file_not_found():
    file_path = 'Not_File.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)