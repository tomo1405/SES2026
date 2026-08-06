import pytest
from src_0731 import task_func

def test_task_func_with_dict():
    data = {'key': 'value'}
    assert task_func(data) == data

def test_task_func_with_list():
    data = [1, 2, 3]
    assert task_func(data) == data

def test_task_func_with_int():
    data = 42
    assert task_func(data) == data

def test_task_func_with_string():
    data = "Hello, World!"
    assert task_func(data) == data

def test_task_func_with_float():
    data = 3.14
    assert task_func(data) == data

def test_task_func_with_none():
    data = None
    assert task_func(data) == data

def test_task_func_with_tuple():
    data = (1, 2, 3)
    assert task_func(data) == data

def test_task_func_with_set():
    data = {1, 2, 3}
    assert task_func(data) == data

def test_task_func_with_custom_object():
    class CustomObject:
        def __init__(self, value):
            self.value = value
        
        def __eq__(self, other):
            return self.value == other.value

    data = CustomObject(10)
    assert task_func(data) == CustomObject(10)