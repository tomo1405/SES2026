import pytest
from src_0720 import task_func

def test_task_func():
    directory = 'path/to/directory'
    word = 'test'
    count = task_func(directory, word)
    assert count == 1

def test_task_func_with_multiple_matches():
    directory = 'path/to/directory'
    word = 'test'
    count = task_func(directory, word)
    assert count == 2

def test_task_func_with_no_matches():
    directory = 'path/to/directory'
    word = 'test'
    count = task_func(directory, word)
    assert count == 0