import pytest
from src_0345 import task_func

def test_task_func_valid_input():
    src_folder = "test_src_folder"
    backup_dir = "test_backup_dir"
    os.makedirs(src_folder)
    os.makedirs(backup_dir)
    assert task_func(src_folder, backup_dir) == True
    assert os.path.isdir(backup_folder)
    assert not os.path.isdir(src_folder)

def test_task_func_invalid_input():
    src_folder = "test_src_folder"
    backup_dir = "test_backup_dir"
    os.makedirs(src_folder)
    os.makedirs(backup_dir)
    with pytest.raises(ValueError):
        task_func(src_folder, backup_dir)
    assert not os.path.isdir(backup_folder)
    assert os.path.isdir(src_folder)