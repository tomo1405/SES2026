import pytest
from src_0799 import task_func

def test_task_func_backup_dir_does_not_exist():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    if os.path.exists(BACKUP_DIR):
        shutil.rmtree(BACKUP_DIR)
    assert task_func(directory) == f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

def test_task_func_no_backups_found():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    assert task_func(directory) == f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

def test_task_func_directory_exists():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    latest_backup = sorted(os.listdir(BACKUP_DIR))[-1]
    shutil.copytree(os.path.join(BACKUP_DIR, latest_backup), directory)
    assert task_func(directory) == directory