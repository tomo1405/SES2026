python
import os
import shutil
import pytest

from src_0345 import task_func

def test_task_func():
    # Test case 1: Source folder does not exist
    with pytest.raises(ValueError):
        task_func("non_existent_folder", "backup_dir")
    
    # Test case 2: Backup folder already exists
    os.makedirs("backup_dir/test_folder", exist_ok=True)
    with pytest.raises(FileExistsError):
        task_func("test_folder", "backup_dir")
    
    # Test case 3: Backup successful
    os.makedirs("test_folder", exist_ok=True)
    assert task_func("test_folder", "backup_dir") == True
    assert os.path.exists("backup_dir/test_folder") == True
    
    # Test case 4: Delete source folder error
    os.makedirs("test_folder/sub_folder", exist_ok=True)
    with pytest.raises(Exception):
        task_func("test_folder", "backup_dir")
    assert os.path.exists("test_folder/sub_folder") == True
    
    # Test case 5: Delete source folder successful
    os.makedirs("test_folder/sub_folder/sub_sub_folder", exist_ok=True)
    assert task_func("test_folder", "backup_dir") == True
    assert os.path.exists("backup_dir/test_folder") == True
    assert os.path.exists("test_folder/sub_folder/sub_sub_folder") == False