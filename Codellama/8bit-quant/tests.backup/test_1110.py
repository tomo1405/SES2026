import pytest
from src_110 import task_func

def test_task_func():
    file_path = 'File.txt'
    tokens = task_func(file_path)
    assert tokens == ['token1', 'token2', 'token3']