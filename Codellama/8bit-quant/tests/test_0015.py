import pytest
from src_0015 import task_func

def test_task_func_valid_config_file():
    config_file_path = 'path/to/config/file'
    archieve_dir = '/home/user/archive'
    assert task_func(config_file_path, archieve_dir) == True

def test_task_func_invalid_config_file():
    config_file_path = 'path/to/invalid/config/file'
    archieve_dir = '/home/user/archive'
    with pytest.raises(FileNotFoundError):
        task_func(config_file_path, archieve_dir)

def test_task_func_invalid_archive_dir():
    config_file_path = 'path/to/config/file'
    archieve_dir = '/home/user/invalid/archive'
    with pytest.raises(Exception):
        task_func(config_file_path, archieve_dir)