import pytest
from src_0723 import task_func

def test_task_func():
    url = 'https://www.example.com'
    occurrences = task_func(url)
    assert occurrences == 0

def test_task_func_with_error():
    url = 'https://www.example.com/error'
    occurrences = task_func(url)
    assert occurrences == 1

def test_task_func_with_multiple_errors():
    url = 'https://www.example.com/error/error'
    occurrences = task_func(url)
    assert occurrences == 2