import pytest
from src_0345 import task_func

def test_task_func():
    # Test case 1: Successful backup
    src_folder = "test_src"
    backup_dir = "test_backup"
    os.makedirs(src_folder)
    assert task_func(src_folder, backup_dir) is True
    assert os.path.isdir(backup_dir)
    shutil.rmtree(src_folder)
    shutil.rmtree(backup_dir)

    # Test case 2: Source folder does not exist
    src_folder = "nonexistent_folder"
    with pytest.raises(ValueError):
        task_func(src_folder, backup_dir)

    # Test case 3: Error during deletion
    src_folder = "test_src"
    os.makedirs(src_folder)
    with pytest.raises(Exception):
        task_func(src_folder, backup_dir)
    assert not os.path.exists(src_folder)
    shutil.rmtree(backup_dir)