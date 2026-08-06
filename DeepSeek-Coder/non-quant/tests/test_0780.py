import pytest
from src_0780 import task_func

def test_task_func_success():
    # Test case for successful backup
    result, errors = task_func("/path/to/directory")
    assert result == "/fake/backup/path"
    assert not errors

def test_task_func_directory_not_exist():
    # Test case for directory not existing
    result, errors = task_func("/nonexistent/directory")
    assert result is None
    assert "Directory does not exist" in errors[0]

def test_task_func_permission_error():
    # Test case for permission error
    result, errors = task_func("/path/to/directory")
    assert result is None
    assert "Permission denied" in errors[0]

def test_task_func_backup_failure():
    # Test case for backup failure
    result, errors = task_func("/path/to/directory")
    assert result is None
    assert "Backup failed" in errors[0]

def test_task_func_restore_failure():
    # Test case for restore failure
    result, errors = task_func("/path/to/directory")
    assert result is None
    assert "Restore failed" in errors[0]