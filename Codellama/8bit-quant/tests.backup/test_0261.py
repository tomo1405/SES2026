import pytest
from src_0261 import task_func

def test_task_func_with_valid_directory():
    directory = 'path/to/directory'
    updated_files = task_func(directory)
    assert updated_files > 0

def test_task_func_with_invalid_directory():
    directory = 'path/to/invalid/directory'
    updated_files = task_func(directory)
    assert updated_files == 0

def test_task_func_with_valid_file():
    file = 'path/to/file.json'
    with open(file, 'w') as f:
        data = {'key': 'value'}
        json.dump(data, f)
    updated_files = task_func(file)
    assert updated_files == 1

def test_task_func_with_invalid_file():
    file = 'path/to/invalid/file.json'
    updated_files = task_func(file)
    assert updated_files == 0