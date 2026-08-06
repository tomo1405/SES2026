import pytest
from src_0799 import task_func

def test_task_func_backup_dir_does_not_exist():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    os.environ['BACKUP_DIR'] = BACKUP_DIR
    os.environ['directory'] = directory
    result = task_func(directory)
    assert result == f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

def test_task_func_no_backups_found():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    os.environ['BACKUP_DIR'] = BACKUP_DIR
    os.environ['directory'] = directory
    result = task_func(directory)
    assert result == f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

def test_task_func_directory_exists():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    os.environ['BACKUP_DIR'] = BACKUP_DIR
    os.environ['directory'] = directory
    result = task_func(directory)
    assert result == directory