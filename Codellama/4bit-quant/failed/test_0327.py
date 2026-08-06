import pytest
from src_0327 import task_func

def test_task_func():
    directory_path = "path/to/directory"
    results = task_func(directory_path)
    assert len(results) == 2
    assert results[0][0] == "file1.bat"
    assert results[0][1] == 0
    assert results[1][0] == "file2.bat"
    assert results[1][1] == 0

def test_task_func_with_invalid_file():
    directory_path = "path/to/directory"
    results = task_func(directory_path)
    assert len(results) == 2
    assert results[0][0] == "file1.bat"
    assert results[0][1] == 0
    assert results[1][0] == "file2.bat"
    assert results[1][1] == 0

def test_task_func_with_invalid_directory():
    directory_path = "path/to/invalid/directory"
    results = task_func(directory_path)
    assert len(results) == 0

def test_task_func_with_invalid_file_path():
    directory_path = "path/to/directory"
    results = task_func(directory_path)
    assert len(results) == 2
    assert results[0][0] == "file1.bat"
    assert results[0][1] == 0
    assert results[1][0] == "file2.bat"
    assert results[1][1] == 0