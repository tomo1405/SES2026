import pytest
from src_0854 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    summary = task_func(directory_path)
    assert summary == {'Invalid': 0, 'txt': 1, 'jpg': 2, 'png': 3}

def test_task_func_invalid_characters():
    directory_path = 'path/to/directory'
    summary = task_func(directory_path)
    assert summary == {'Invalid': 1, 'txt': 1, 'jpg': 2, 'png': 3}

def test_task_func_invalid_directory():
    directory_path = 'path/to/invalid/directory'
    summary = task_func(directory_path)
    assert summary == {'Invalid': 0, 'txt': 1, 'jpg': 2, 'png': 3}

def test_task_func_invalid_file():
    directory_path = 'path/to/directory'
    summary = task_func(directory_path)
    assert summary == {'Invalid': 1, 'txt': 1, 'jpg': 2, 'png': 3}