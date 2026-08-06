import pytest
from src_0337 import task_func

def test_task_func():
    pattern = "hello"
    directory = "."
    extensions = ["*.txt"]
    expected_files = [Path("hello.txt").resolve()]
    assert task_func(pattern, directory, extensions) == expected_files

def test_task_func_with_multiple_extensions():
    pattern = "hello"
    directory = "."
    extensions = ["*.txt", "*.py"]
    expected_files = [Path("hello.txt").resolve(), Path("hello.py").resolve()]
    assert task_func(pattern, directory, extensions) == expected_files

def test_task_func_with_no_matching_files():
    pattern = "hello"
    directory = "."
    extensions = ["*.txt"]
    expected_files = []
    assert task_func(pattern, directory, extensions) == expected_files

def test_task_func_with_invalid_directory():
    pattern = "hello"
    directory = "invalid_directory"
    extensions = ["*.txt"]
    expected_files = []
    assert task_func(pattern, directory, extensions) == expected_files

def test_task_func_with_invalid_pattern():
    pattern = "invalid_pattern"
    directory = "."
    extensions = ["*.txt"]
    expected_files = []
    assert task_func(pattern, directory, extensions) == expected_files