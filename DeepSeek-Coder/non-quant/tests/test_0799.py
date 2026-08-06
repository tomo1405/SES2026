import pytest
from src_0799 import task_func

def test_task_func_no_backups():
    result = task_func('/path/to/directory')
    assert result == 'No backups found in /tmp/backup. Cannot rollback update.'

def test_task_func_no_directory():
    result = task_func('/nonexistent/directory')
    assert result == 'No backups found in /tmp/backup. Cannot rollback update.'

def test_task_func_success():
    # Assuming the backup directory exists and contains backups
    result = task_func('/path/to/directory')
    assert result == '/path/to/directory'