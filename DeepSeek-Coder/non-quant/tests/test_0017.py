import pytest
from src_0017 import task_func

def test_task_func_no_logs():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')

def test_task_func_no_logs_in_directory():
    result = task_func('tests/test_directory_no_logs')
    assert result == "No logs found to backup"

def test_task_func_with_logs():
    result = task_func('tests/test_directory_with_logs')
    assert result == 'backup_file_path'  # Replace with the actual expected result