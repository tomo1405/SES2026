import pickle
import os
import random
import string
from src_0730 import task_func
import pytest

def test_task_func_with_strings():
    strings = ['apple', 'banana', 'cherry']
    loaded_strings = task_func(strings)
    assert loaded_strings == strings

def test_task_func_with_empty_list():
    strings = []
    loaded_strings = task_func(strings)
    assert loaded_strings == strings

def test_task_func_with_none():
    strings = None
    with pytest.raises(TypeError):
        task_func(strings)

def test_task_func_with_filename():
    strings = ['date', 'fig', 'grape']
    filename = 'test.pkl'
    loaded_strings = task_func(strings, filename)
    assert loaded_strings == strings
    os.remove(filename)

def test_task_func_with_invalid_filename():
    strings = ['elderberry', 'fig', 'honeydew']
    filename = 123
    with pytest.raises(TypeError):
        task_func(strings, filename)