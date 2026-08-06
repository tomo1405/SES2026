import os
import glob
import subprocess
from src_0017 import task_func

def test_task_func_with_valid_directory():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    expected_backup_file = '/path/to/backup/logs_backup.tar.gz'
    assert task_func(directory, backup_dir) == expected_backup_file

def test_task_func_with_invalid_directory():
    directory = '/path/to/invalid_directory'
    backup_dir = '/path/to/backup'
    with pytest.raises(FileNotFoundError):
        task_func(directory, backup_dir)

def test_task_func_with_no_logs():
    directory = '/path/to/empty_directory'
    backup_dir = '/path/to/backup'
    expected_output = "No logs found to backup"
    assert task_func(directory, backup_dir) == expected_output

def test_task_func_with_no_backup_dir():
    directory = '/path/to/logs'
    backup_dir = '/path/to/invalid_backup_dir'
    expected_backup_file = '/path/to/invalid_backup_dir/logs_backup.tar.gz'
    assert task_func(directory, backup_dir) == expected_backup_file

def test_task_func_with_existing_backup_dir():
    directory = '/path/to/logs'
    backup_dir = '/path/to/existing_backup_dir'
    os.makedirs(backup_dir, exist_ok=True)
    expected_backup_file = '/path/to/existing_backup_dir/logs_backup.tar.gz'
    assert task_func(directory, backup_dir) == expected_backup_file