import os
import shutil
from src_0780 import task_func

BACKUP_DIR = '/tmp/backup'

def test_task_func_valid_directory():
    directory = "/fake/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert len(errors) == 0

def test_task_func_invalid_directory():
    directory = "/nonexistent/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert len(errors) == 2
    assert errors[0] == "Directory does not exist: /nonexistent/directory"
    assert errors[1] == "Directory does not exist: /nonexistent/directory"

def test_task_func_backup_error():
    directory = "/fake/directory"
    backup_dir = "/fake/backup/path"
    shutil.rmtree(backup_dir)  # Simulate backup error
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert len(errors) == 1
    assert errors[0] == "Directory does not exist: /tmp/backup"

def test_task_func_cleanup_error():
    directory = "/fake/directory"
    backup_dir = "/fake/backup/path"
    os.makedirs(backup_dir)
    os.chmod(backup_dir, 0o444)  # Make backup directory read-only
    shutil.copytree(directory, os.path.join(backup_dir, os.path.basename(directory)))
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert len(errors) == 1
    assert errors[0] == "Permission denied: [Errno 13] Permission denied: '/tmp/backup'"
    os.chmod(backup_dir, 0o755)  # Restore original permissions