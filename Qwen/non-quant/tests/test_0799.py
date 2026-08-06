import pytest
from src_0799 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_backup_dir():
    temp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir, 'backup'))
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def create_backup(setup_backup_dir):
    backup_dir = os.path.join(setup_backup_dir, 'backup')
    backup_path = os.path.join(backup_dir, 'backup_1')
    os.makedirs(backup_path)
    with open(os.path.join(backup_path, 'test_file.txt'), 'w') as f:
        f.write('This is a test file.')
    return backup_dir, backup_path

@pytest.fixture
def target_directory(setup_backup_dir):
    target_path = os.path.join(setup_backup_dir, 'target')
    os.makedirs(target_path)
    with open(os.path.join(target_path, 'original_file.txt'), 'w') as f:
        f.write('This is the original file.')
    return target_path

def test_backup_dir_not_exists(setup_backup_dir):
    backup_dir = os.path.join(setup_backup_dir, 'non_existent_backup')
    assert task_func(backup_dir) == f'Backup directory {backup_dir} does not exist. Cannot rollback update.'

def test_no_backups_found(create_backup):
    backup_dir, _ = create_backup
    shutil.rmtree(backup_dir)
    assert task_func(backup_dir) == f'No backups found in {backup_dir}. Cannot rollback update.'

def test_successful_rollback(create_backup, target_directory):
    backup_dir, backup_path = create_backup
    result = task_func(target_directory)
    assert result == target_directory
    assert os.path.exists(os.path.join(target_directory, 'test_file.txt'))
    assert not os.path.exists(os.path.join(target_directory, 'original_file.txt'))

def test_target_directory_exists(create_backup, target_directory):
    backup_dir, _ = create_backup
    task_func(target_directory)
    assert not os.path.exists(target_directory)

def test_target_directory_does_not_exist(create_backup):
    backup_dir, backup_path = create_backup
    target_path = os.path.join(os.path.dirname(backup_dir), 'new_target')
    result = task_func(target_path)
    assert result == target_path
    assert os.path.exists(os.path.join(target_path, 'test_file.txt'))