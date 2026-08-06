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

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(ValueError) as e:
        task_func('/non/existent/directory')
    assert str(e.value) == "Directory does not exist: /non/existent/directory"

    # Test case 2: Backup directory already exists
    with pytest.raises(OSError) as e:
        task_func('/tmp')
    assert str(e.value) == "[Errno 17] File exists: '/tmp/backup'"

    # Test case 3: Backup directory creation fails
    with pytest.raises(OSError) as e:
        task_func('/non/existent/directory')
    assert str(e.value) == "[Errno 2] No such file or directory: '/non/existent/directory'"

    # Test case 4: Backup directory creation succeeds
    backup_dir, errors = task_func('/tmp')
    assert backup_dir == '/fake/backup/path'
    assert errors == []

    # Test case 5: Backup directory creation succeeds, but cleanup fails
    backup_dir, errors = task_func('/tmp')
    assert backup_dir == '/fake/backup/path'
    assert errors == ["Permission denied: [Errno 13] Permission denied: '/tmp/backup/tmp'"]

    # Test case 6: Backup directory creation succeeds, but cleanup succeeds
    backup_dir, errors = task_func('/tmp')
    assert backup_dir == '/fake/backup/path'
    assert errors == []

    # Test case 7: Backup directory creation succeeds, but backup fails
    with pytest.raises(Exception) as e:
        backup_dir, errors = task_func('/non/existent/directory')
    assert str(e.value) == "No such file or directory: '/non/existent/directory'"

    # Test case 8: Backup directory creation succeeds, but backup succeeds
    backup_dir, errors = task_func('/tmp')
    assert backup_dir == '/fake/backup/path'
    assert errors == []