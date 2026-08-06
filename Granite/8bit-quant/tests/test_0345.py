import os
import shutil
import pytest
from src_0345 import task_func

def test_task_func_valid_input():
    src_folder = "/path/to/source/folder"
    backup_dir = "/path/to/backup/directory"
    assert task_func(src_folder, backup_dir) == True

def test_task_func_invalid_input():
    src_folder = "/path/to/source/folder"
    backup_dir = "/path/to/backup/directory"
    with pytest.raises(ValueError):
        task_func(src_folder, backup_dir)

def test_task_func_backup_folder_exists():
    src_folder = "/path/to/source/folder"
    backup_dir = "/path/to/backup/directory"
    os.makedirs(os.path.join(backup_dir, os.path.basename(src_folder)))
    assert task_func(src_folder, backup_dir) == False

def test_task_func_delete_source_folder_error():
    src_folder = "/path/to/source/folder"
    backup_dir = "/path/to/backup/directory"
    with pytest.raises(Exception):
        task_func(src_folder, backup_dir)