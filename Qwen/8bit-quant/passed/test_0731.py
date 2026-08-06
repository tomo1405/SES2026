import pytest
from src_0731 import task_func
import os

def test_task_func_with_dict():
    data = {'key': 'value'}
    result = task_func(data)
    assert result == data

def test_task_func_with_list():
    data = [1, 2, 3]
    result = task_func(data)
    assert result == data

def test_task_func_with_int():
    data = 42
    result = task_func(data)
    assert result == data

def test_task_func_with_string():
    data = "Hello, World!"
    result = task_func(data)
    assert result == data

def test_task_func_with_none():
    data = None
    result = task_func(data)
    assert result == data

def test_file_not_created_after_function():
    task_func({'test': 'data'})
    assert not os.path.exists('save.pkl')