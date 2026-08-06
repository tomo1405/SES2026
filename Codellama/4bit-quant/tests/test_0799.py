import os
import shutil

from src_0799 import task_func


def test_task_func_backup_dir_does_not_exist():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    backup_dir_exists = os.path.exists(BACKUP_DIR)
    assert backup_dir_exists == True
    result = task_func(directory)
    assert result == f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

def test_task_func_no_backups_found():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    backups = sorted(os.listdir(BACKUP_DIR))
    latest_backup = backups[-1] if backups else None
    if not latest_backup:
        result = task_func(directory)
        assert result == f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

def test_task_func_directory_exists():
    directory = '/tmp/test_dir'
    BACKUP_DIR = '/tmp/backup'
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    backups = sorted(os.listdir(BACKUP_DIR))
    latest_backup = backups[-1] if backups else None
    if os.path.exists(directory):
        shutil.rmtree(directory)
    shutil.copytree(os.path.join(BACKUP_DIR, latest_backup), directory)
    result = task_func(directory)
    assert result == directory