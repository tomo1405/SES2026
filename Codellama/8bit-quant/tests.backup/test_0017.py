import pytest
from src_0017 import task_func

def test_task_func_valid_directory():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    backup_file = task_func(directory, backup_dir)
    assert backup_file == os.path.join(backup_dir, 'logs_backup.tar.gz')

def test_task_func_invalid_directory():
    directory = '/path/to/invalid'
    backup_dir = '/path/to/backup'
    with pytest.raises(FileNotFoundError):
        task_func(directory, backup_dir)

def test_task_func_no_logs():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    backup_file = task_func(directory, backup_dir)
    assert backup_file == "No logs found to backup"

def test_task_func_backup_file_exists():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    backup_file = task_func(directory, backup_dir)
    assert os.path.exists(backup_file)

def test_task_func_logs_deleted():
    directory = '/path/to/logs'
    backup_dir = '/path/to/backup'
    backup_file = task_func(directory, backup_dir)
    for file in glob.glob(os.path.join(directory, '*.log')):
        assert not os.path.exists(file)