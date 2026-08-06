import pytest
from src_0720 import task_func

def test_task_func():
    directory = 'path/to/directory'
    word = 'test'
    count = task_func(directory, word)
    assert count == 1

def test_task_func_case_insensitive():
    directory = 'path/to/directory'
    word = 'Test'
    count = task_func(directory, word)
    assert count == 1

def test_task_func_punctuation():
    directory = 'path/to/directory'
    word = 'test.'
    count = task_func(directory, word)
    assert count == 1

def test_task_func_multiple_files():
    directory = 'path/to/directory'
    word = 'test'
    count = task_func(directory, word)
    assert count == 2

def test_task_func_no_match():
    directory = 'path/to/directory'
    word = 'no_match'
    count = task_func(directory, word)
    assert count == 0