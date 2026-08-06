import pytest
from src_0327 import task_func

def test_task_func_with_valid_directory_path():
    directory_path = "path/to/directory"
    results = task_func(directory_path)
    assert len(results) > 0
    for result in results:
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], str)
        assert isinstance(result[1], int)

def test_task_func_with_invalid_directory_path():
    directory_path = "path/to/invalid/directory"
    results = task_func(directory_path)
    assert len(results) == 0

def test_task_func_with_valid_file_path():
    file_path = "path/to/file.bat"
    results = task_func(file_path)
    assert len(results) == 1
    assert results[0][0] == "file.bat"
    assert results[0][1] == 0

def test_task_func_with_invalid_file_path():
    file_path = "path/to/invalid/file.bat"
    results = task_func(file_path)
    assert len(results) == 0