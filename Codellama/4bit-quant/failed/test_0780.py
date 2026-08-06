import pytest
from src_0780 import task_func

def test_task_func_valid_directory():
    directory = "/path/to/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert not errors

def test_task_func_invalid_directory():
    directory = "/path/to/invalid/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert errors == ["Directory does not exist: /path/to/invalid/directory"]

def test_task_func_permission_denied():
    directory = "/path/to/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert errors == ["Permission denied: PermissionError('Permission denied: /path/to/directory')"]

def test_task_func_exception():
    directory = "/path/to/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert errors == ["Exception: Exception('Exception')"]