import os
import shutil
import pytest

from src_0345 import task_func

def test_task_func():
    src_folder = "/path/to/source/folder"
    backup_dir = "/path/to/backup/directory"
    
    # Test if source folder exists
    with pytest.raises(ValueError) as exc_info:
        task_func(src_folder, "invalid_backup_dir")
    assert "Source folder 'invalid_backup_dir' does not exist." in str(exc_info.value)
    
    # Test if backup folder is created successfully
    task_func(src_folder, backup_dir)
    backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
    assert os.path.isdir(backup_folder)
    
    # Test if source folder is deleted successfully
    assert task_func(src_folder, backup_dir)
    assert not os.path.isdir(src_folder)
    
    # Test if exception is raised while deleting source folder
    with pytest.raises(Exception) as exc_info:
        task_func(src_folder, backup_dir)
    assert "Error while deleting source folder" in str(exc_info.value)