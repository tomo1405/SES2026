import pytest
from src_0973 import task_func

def test_task_func_empty_path():
    assert task_func("") == []

def test_task_func_invalid_path():
    assert task_func("path/to/invalid/file") == []

def test_task_func_valid_path():
    assert task_func("path/to/valid/file") == ["path", "to", "valid", "file"]

def test_task_func_path_with_delimiter():
    assert task_func("path/to/valid/file", delimiter=".") == ["path", "to", "valid", "file"]

def test_task_func_path_with_invalid_characters():
    assert task_func("path/to/invalid/file<") == []

def test_task_func_path_with_invalid_characters_and_delimiter():
    assert task_func("path/to/invalid/file<", delimiter=".") == []