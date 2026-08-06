import pytest
from src_0799 import task_func
import os
import shutil
import tempfile

def setup_module():
    # Create a temporary backup directory
    global BACKUP_DIR
    BACKUP_DIR = tempfile.mkdtemp()

def teardown_module():
    # Remove the temporary backup directory
    if os.path.exists(BACKUP_DIR):
        shutil.rmtree(BACKUP_DIR)

def test_task_func_no_backup_dir():
    # Test case: Backup directory does not exist
    non_existent_dir = '/non/existent/dir'
    result = task_func(non_existent_dir)
    assert result == f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

def test_task_func_no_backups():
    # Test case: No backups found in the backup directory
    result = task_func('/test/directory')
    assert result == f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

def test_task_func_with_backup():
    # Test case: Backup directory exists and contains a backup
    test_dir = tempfile.mkdtemp()
    backup_subdir = os.path.join(BACKUP_DIR, 'backup_1')
    os.makedirs(backup_subdir)
    with open(os.path.join(backup_subdir, 'testfile.txt'), 'w') as f:
        f.write('This is a test file.')

    result = task_func(test_dir)
    assert os.path.exists(os.path.join(test_dir, 'testfile.txt'))
    assert result == test_dir

    # Clean up the test directory
    shutil.rmtree(test_dir)

def test_task_func_overwrite_existing_directory():
    # Test case: The target directory already exists and should be overwritten
    test_dir = tempfile.mkdtemp()
    with open(os.path.join(test_dir, 'existing_file.txt'), 'w') as f:
        f.write('Existing file content.')

    backup_subdir = os.path.join(BACKUP_DIR, 'backup_2')
    os.makedirs(backup_subdir)
    with open(os.path.join(backup_subdir, 'new_file.txt'), 'w') as f:
        f.write('New file content.')

    result = task_func(test_dir)
    assert not os.path.exists(os.path.join(test_dir, 'existing_file.txt'))
    assert os.path.exists(os.path.join(test_dir, 'new_file.txt'))
    assert result == test_dir

    # Clean up the test directory
    shutil.rmtree(test_dir)