import os
import shutil
from src_0345 import task_func

def test_task_func_valid_input():
    src_folder = "/path/to/source/folder"
    backup_dir = "/path/to/backup/directory"
    assert task_func(src_folder, backup_dir) == True

def test_task_func_invalid_input():
    src_folder = "/path/to/nonexistent/folder"
    backup_dir = "/path/to/backup/directory"
    with pytest.raises(ValueError) as exc_info:
        task_func(src_folder, backup_dir)
    assert "Source folder" in str(exc_info.value)

def test_task_func_backup_and_delete():
    src_folder = "/path/to/source/folder"
    backup_dir = "/path/to/backup/directory"
    task_func(src_folder, backup_dir)
    backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
    assert os.path.isdir(backup_folder)
    shutil.rmtree(src_folder)