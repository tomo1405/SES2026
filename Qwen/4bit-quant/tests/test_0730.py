import pytest
from src_0730 import task_func
import os
import tempfile

def test_task_func_with_default_filename():
    strings = ["hello", "world"]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_custom_filename():
    strings = ["foo", "bar"]
    temp_dir = tempfile.mkdtemp()
    filename = os.path.join(temp_dir, "test_file.pkl")
    result = task_func(strings, filename)
    assert result == strings
    assert not os.path.exists(filename), "File should be deleted after loading"

def test_task_func_with_nonexistent_directory():
    strings = ["baz", "qux"]
    temp_dir = tempfile.mkdtemp()
    filename = os.path.join(temp_dir, "nonexistent_dir", "test_file.pkl")
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
    strings = ["!@#", "$%^", "&*()"]
    result = task_func(strings)
    assert result == strings

def test_task_func_with_large_list():
    strings = [str(i) for i in range(1000)]
    result = task_func(strings)
    assert result == strings