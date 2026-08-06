from collections import Counter

import pytest
from src_0962 import task_func


def test_task_func_valid_directory():
    directory = "/path/to/valid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True
    result = task_func(directory, extensions, keep_zero)
    assert isinstance(result, Counter)

def test_task_func_invalid_directory():
    directory = "/path/to/invalid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True
    with pytest.raises(OSError):
        task_func(directory, extensions, keep_zero)

def test_task_func_valid_extensions():
    directory = "/path/to/valid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True
    result = task_func(directory, extensions, keep_zero)
    assert all(ext in result for ext in extensions)

def test_task_func_invalid_extensions():
    directory = "/path/to/valid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv", ".invalid"]
    keep_zero = True
    result = task_func(directory, extensions, keep_zero)
    assert all(ext in result for ext in extensions[:-1])

def test_task_func_keep_zero():
    directory = "/path/to/valid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True
    result = task_func(directory, extensions, keep_zero)
    assert all(count >= 0 for count in result.values())

def test_task_func_no_keep_zero():
    directory = "/path/to/valid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = False
    result = task_func(directory, extensions, keep_zero)
    assert all(count > 0 for count in result.values())