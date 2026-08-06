import pytest
from src_0973 import task_func

def test_task_func_valid_path():
    path = "path/to/file.txt"
    delimiter = "/"
    expected_result = ["path", "to", "file.txt"]
    assert task_func(path, delimiter) == expected_result

def test_task_func_invalid_path():
    path = "path/to/file.txt"
    delimiter = "/"
    expected_result = []
    assert task_func(path, delimiter) == expected_result

def test_task_func_invalid_delimiter():
    path = "path/to/file.txt"
    delimiter = "\\"
    expected_result = []
    assert task_func(path, delimiter) == expected_result

def test_task_func_empty_path():
    path = ""
    delimiter = "/"
    expected_result = []
    assert task_func(path, delimiter) == expected_result

def test_task_func_invalid_characters():
    path = "path/to/file.txt"
    delimiter = "/"
    expected_result = []
    assert task_func(path, delimiter) == expected_result