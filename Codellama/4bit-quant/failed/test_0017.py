import pytest
from src_0017 import task_func

def test_task_func_valid_directory():
    directory = '/path/to/directory'
    backup_dir = '/path/to/backup'
    assert task_func(directory, backup_dir) == 'No logs found to backup'

def test_task_func_invalid_directory():
    directory = '/path/to/invalid/directory'
    backup_dir = '/path/to/backup'
    with pytest.raises(FileNotFoundError):
        task_func(directory, backup_dir)

def test_task_func_valid_backup_dir():
    directory = '/path/to/directory'
    backup_dir = '/path/to/backup'
    assert task_func(directory, backup_dir) == 'No logs found to backup'

def test_task_func_invalid_backup_dir():
    directory = '/path/to/directory'
    backup_dir = '/path/to/invalid/backup'
    with pytest.raises(FileNotFoundError):
        task_func(directory, backup_dir)

def test_task_func_valid_log_files():
    directory = '/path/to/directory'
    backup_dir = '/path/to/backup'
    log_files = ['/path/to/log1.log', '/path/to/log2.log']
    assert task_func(directory, backup_dir) == 'No logs found to backup'

def test_task_func_invalid_log_files():
    directory = '/path/to/directory'
    backup_dir = '/path/to/backup'
    log_files = ['/path/to/invalid/log1.log', '/path/to/invalid/log2.log']
    with pytest.raises(FileNotFoundError):
        task_func(directory, backup_dir)