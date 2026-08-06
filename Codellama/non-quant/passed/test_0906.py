import pytest
from src_0906 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    file_extension = '.csv'
    data = task_func(directory_path, file_extension)
    assert isinstance(data, dict)
    assert all(isinstance(key, str) and isinstance(value, list) for key, value in data.items())
    assert all(len(value) > 0 for value in data.values())