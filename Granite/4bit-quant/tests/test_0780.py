import os
import shutil
from src_0780 import task_func

BACKUP_DIR = '/tmp/backup'

def test_task_func_with_existing_directory():
    directory = "/fake/directory"
    os.makedirs(directory)
    backup_dir, errors = task_func(directory)
    assert backup_dir == "/fake/backup/path"
    assert errors == []

def test_task_func_with_non_existing_directory():
    directory = "/non/existing/directory"
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert errors == ["Directory does not exist: /non/existing/directory"]

def test_task_func_with_permission_error():
    directory = "/permission/denied/directory"
    os.makedirs(directory)
    os.chmod(directory, 0o400)
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert errors == ["Permission denied: [Errno 13] Permission denied: '/permission/denied/directory'"]
    os.chmod(directory, 0o755)

def test_task_func_with_exception():
    directory = "/exception/directory"
    os.makedirs(directory)
    backup_dir, errors = task_func(directory)
    assert backup_dir is None
    assert errors == ["An unexpected error occurred: 'NoneType' object has no attribute 'rmtree'"]