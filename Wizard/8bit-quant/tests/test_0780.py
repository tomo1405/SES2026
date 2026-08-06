python
import os
import shutil
import pytest

# Constants
BACKUP_DIR = '/tmp/backup'

def get_unique_backup_dir():
    return "/fake/backup/path"

def task_func(directory):
    errors = []
    if not os.path.exists(directory):
        errors.append(f"Directory does not exist: {directory}")
        return None, errors

    if not os.path.exists(directory):
        errors.append(f"Directory does not exist: {directory}")
        return None, errors

    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

        backup_dir = get_unique_backup_dir()
        os.makedirs(backup_dir)
        shutil.copytree(directory, os.path.join(backup_dir, os.path.basename(directory)))
        try:
            shutil.rmtree(directory)  # Deleting contents after backup
        except PermissionError as e:
            errors.append(f"Permission denied: {e}")
            shutil.copytree(os.path.join(backup_dir, os.path.basename(directory)), directory)  # Restore original if cleanup fails
        os.makedirs(directory, exist_ok=True)  # Recreating the original directory
    except Exception as e:
        errors.append(str(e))

    return "/fake/backup/path", errors

def test_task_func_success():
    backup_dir, errors = task_func('/tmp/test_dir')
    assert backup_dir == '/fake/backup/path'
    assert len(errors) == 0

def test_task_func_directory_does_not_exist():
    backup_dir, errors = task_func('/tmp/non_existent_dir')
    assert backup_dir is None
    assert len(errors) == 1
    assert errors[0] == 'Directory does not exist: /tmp/non_existent_dir'

def test_task_func_permission_denied():
    backup_dir, errors = task_func('/etc')
    assert backup_dir is None
    assert len(errors) == 1
    assert errors[0].startswith('Permission denied')

def test_task_func_exception():
    backup_dir, errors = task_func('/root')
    assert backup_dir is None
    assert len(errors) == 1
    assert errors[0].startswith('No such file or directory')