import pytest
from src_0799 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_backup_dir():
    temp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir, 'backup'))
    yield os.path.join(temp_dir, 'backup')
    shutil.rmtree(temp_dir)

@pytest.fixture
def setup_directory():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func_no_backup_dir(setup_directory):
    result = task_func(setup_directory)
    assert result == f'Backup directory {os.path.join(setup_directory, "backup")} does not exist. Cannot rollback update.'

def test_task_func_no_backups(setup_backup_dir, setup_directory):
    result = task_func(setup_directory)
    assert result == f'No backups found in {setup_backup_dir}. Cannot rollback update.'

def test_task_func_with_backup(setup_backup_dir, setup_directory):
    backup_content = {'file1.txt': 'content1', 'file2.txt': 'content2'}
    latest_backup = 'backup_1'
    os.makedirs(os.path.join(setup_backup_dir, latest_backup))
    for filename, content in backup_content.items():
        with open(os.path.join(setup_backup_dir, latest_backup, filename), 'w') as f:
            f.write(content)

    result = task_func(setup_directory)
    assert result == setup_directory
    for filename, content in backup_content.items():
        with open(os.path.join(setup_directory, filename), 'r') as f:
            assert f.read() == content

def test_task_func_directory_exists(setup_backup_dir, setup_directory):
    os.makedirs(setup_directory)
    with open(os.path.join(setup_directory, 'existing_file.txt'), 'w') as f:
        f.write('Existing file content')

    backup_content = {'file1.txt': 'content1', 'file2.txt': 'content2'}
    latest_backup = 'backup_1'
    os.makedirs(os.path.join(setup_backup_dir, latest_backup))
    for filename, content in backup_content.items():
        with open(os.path.join(setup_backup_dir, latest_backup, filename), 'w') as f:
            f.write(content)

    result = task_func(setup_directory)
    assert result == setup_directory
    assert not os.path.exists(os.path.join(setup_directory, 'existing_file.txt'))
    for filename, content in backup_content.items():
        with open(os.path.join(setup_directory, filename), 'r') as f:
            assert f.read() == content