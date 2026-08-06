import pytest
from src_0017 import task_func

def test_task_func_valid_directory():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    assert task_func(directory, backup_dir) == 'No logs found to backup'

def test_task_func_invalid_directory():
    directory = '/path/to/invalid/directory'
    backup_dir = '/path/to/backup'
    with pytest.raises(FileNotFoundError):
        task_func(directory, backup_dir)

def test_task_func_backup_file():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    assert task_func(directory, backup_dir) == 'No logs found to backup'
    assert os.path.exists(os.path.join(backup_dir, 'logs_backup.tar.gz'))

def test_task_func_remove_files():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    assert task_func(directory, backup_dir) == 'No logs found to backup'
    assert not os.path.exists(os.path.join(directory, '*.log'))