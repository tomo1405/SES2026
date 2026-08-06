import pytest
from src_0345 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_folders():
    src_folder = tempfile.mkdtemp()
    backup_dir = tempfile.mkdtemp()
    yield src_folder, backup_dir
    shutil.rmtree(src_folder)
    shutil.rmtree(backup_dir)

def test_task_func_valid_input(setup_folders):
    src_folder, backup_dir = setup_folders
    file_path = os.path.join(src_folder, 'test_file.txt')
    with open(file_path, 'w') as f:
        f.write('Test content')
    
    result = task_func(src_folder, backup_dir)
    
    assert result is True
    assert not os.path.exists(src_folder)
    assert os.path.exists(os.path.join(backup_dir, os.path.basename(src_folder), 'test_file.txt'))

def test_task_func_nonexistent_source_folder():
    with pytest.raises(ValueError) as exc_info:
        task_func('/nonexistent_folder', '/backup_dir')
    
    assert str(exc_info.value) == "Source folder '/nonexistent_folder' does not exist."

def test_task_func_backup_failure(setup_folders, monkeypatch):
    src_folder, backup_dir = setup_folders
    
    def mock_copytree(src, dst):
        raise PermissionError("Mocked permission error")
    
    monkeypatch.setattr(shutil, 'copytree', mock_copytree)
    
    result = task_func(src_folder, backup_dir)
    
    assert result is False
    assert os.path.exists(src_folder)

def test_task_func_delete_failure(setup_folders, monkeypatch):
    src_folder, backup_dir = setup_folders
    file_path = os.path.join(src_folder, 'test_file.txt')
    with open(file_path, 'w') as f:
        f.write('Test content')
    
    def mock_rmtree(path):
        raise PermissionError("Mocked permission error")
    
    monkeypatch.setattr(shutil, 'rmtree', mock_rmtree)
    
    result = task_func(src_folder, backup_dir)
    
    assert result is False
    assert os.path.exists(src_folder)