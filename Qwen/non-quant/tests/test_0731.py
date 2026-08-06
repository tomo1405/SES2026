import pytest
from src_0731 import task_func
import os
import pickle

def test_task_func_with_int():
    data = 42
    result = task_func(data)
    assert result == data

def test_task_func_with_string():
    data = "Hello, World!"
    result = task_func(data)
    assert result == data

def test_task_func_with_list():
    data = [1, 2, 3, 4, 5]
    result = task_func(data)
    assert result == data

def test_task_func_with_dict():
    data = {'key': 'value'}
    result = task_func(data)
    assert result == data

def test_task_func_with_tuple():
    data = (1, 2, 3)
    result = task_func(data)
    assert result == data

def test_task_func_with_set():
    data = {1, 2, 3}
    result = task_func(data)
    assert result == data

def test_task_func_with_custom_object():
    class CustomObject:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    data = CustomObject(42)
    result = task_func(data)
    assert result == data

def test_task_func_file_not_created_afterwards():
    data = "Test Data"
    task_func(data)
    assert not os.path.exists('save.pkl')