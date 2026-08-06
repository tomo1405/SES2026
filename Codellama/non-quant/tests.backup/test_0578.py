import pytest
from src_0578 import task_func

def test_task_func():
    directory = 'path/to/directory'
    files_info = task_func(directory)

    assert isinstance(files_info, dict)
    assert all(isinstance(key, str) for key in files_info.keys())
    assert all(isinstance(value, dict) for value in files_info.values())
    assert all(key in value for key in ['Size', 'MD5 Hash'] for value in files_info.values())
    assert all(isinstance(value['Size'], int) for value in files_info.values())
    assert all(isinstance(value['MD5 Hash'], str) for value in files_info.values())