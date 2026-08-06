python
import os
import shutil
import pytest

from src_0345 import task_func

def test_task_func():
    # Test case 1: Source folder does not exist
    with pytest.raises(ValueError):
        task_func("nonexistent_folder", "backup_dir")
    
    # Test case 2: Backup folder already exists
    os.makedirs("backup_dir/test_folder", exist_ok=True)
    with pytest.raises(FileExistsError):
        task_func("test_folder", "backup_dir")
    
    # Test case 3: Backup folder created successfully
    os.makedirs("test_folder", exist_ok=True)
    assert task_func("test_folder", "backup_dir") == True
    assert os.path.isdir("backup_dir/test_folder") == True
    
    # Test case 4: Source folder deleted successfully
    assert task_func("backup_dir/test_folder", "backup_dir") == True
    assert os.path.isdir("backup_dir/test_folder") == False