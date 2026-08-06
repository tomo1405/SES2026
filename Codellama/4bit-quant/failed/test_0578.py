import pytest
from src_0578 import task_func

def test_task_func():
    directory = 'path/to/directory'
    files_info = task_func(directory)
    assert isinstance(files_info, dict)
    for file_name, file_info in files_info.items():
        assert isinstance(file_name, str)
        assert isinstance(file_info, dict)
        assert 'Size' in file_info
        assert 'MD5 Hash' in file_info
        assert isinstance(file_info['Size'], int)
        assert isinstance(file_info['MD5 Hash'], str)