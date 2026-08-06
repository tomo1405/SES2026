import pytest
from src_0730 import task_func
import os
import pickle

def test_task_func_with_filename():
    strings = ["hello", "world"]
    filename = "test_file.pkl"
    
    result = task_func(strings, filename=filename)
    
    assert result == strings
    assert not os.path.exists(filename)

def test_task_func_without_filename():
    strings = ["foo", "bar"]
    
    result = task_func(strings)
    
    assert result == strings

def test_task_func_with_empty_list():
    strings = []
    
    result = task_func(strings)
    
    assert result == strings

def test_task_func_with_single_string():
    strings = ["single"]
    
    result = task_func(strings)
    
    assert result == strings

def test_task_func_with_non_string_elements():
    strings = [1, 2, 3]
    
    result = task_func(strings)
    
    assert result == strings

def test_task_func_with_special_characters():
    strings = ["@#%", "!$^"]
    
    result = task_func(strings)
    
    assert result == strings