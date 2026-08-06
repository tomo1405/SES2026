import pytest
from src_0730 import task_func
import os
import pickle

def test_task_func_with_default_filename():
    strings = ["hello", "world"]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_custom_filename():
    strings = ["foo", "bar"]
    filename = "test_file.pkl"
    result = task_func(strings, filename)
    assert result == strings
    assert not os.path.exists(filename)

def test_task_func_with_nonexistent_directory():
    strings = ["baz", "qux"]
    filename = "/nonexistent/directory/test_file.pkl"
    with pytest.raises(FileNotFoundError):
        task_func(strings, filename)

def test_task_func_with_empty_list():
    strings = []
    result = task_func(strings)
    assert result == strings

def test_task_func_with_single_string():
    strings = ["single"]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_special_characters():
    strings = ["@#$%", "!@#"]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_large_strings():
    strings = [''.join(random.choices(string.ascii_letters, k=1000)) for _ in range(10)]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_nested_lists():
    strings = [["nested", "list"], ["another", "list"]]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_none():
    strings = [None]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_mixed_data_types():
    strings = [123, "string", 456.789, True]
    result = task_func(strings)
    assert result == strings