import os
import shutil
import pytest

from src_0119 import task_func

def test_task_func():
    directory = "/path/to/directory"
    backup_directory = "/path/to/backup_directory"
    copied_files = task_func(directory, backup_directory)

    assert isinstance(copied_files, list)
    for filename in copied_files:
        assert os.path.exists(filename)

def test_task_func_with_nonexistent_directory():
    directory = "/path/to/nonexistent_directory"
    backup_directory = "/path/to/backup_directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory, backup_directory)

def test_task_func_with_nonexistent_backup_directory():
    directory = "/path/to/directory"
    backup_directory = "/path/to/nonexistent_backup_directory"
    os.makedirs(backup_directory, exist_ok=True)
    copied_files = task_func(directory, backup_directory)

    assert isinstance(copied_files, list)
    for filename in copied_files:
        assert os.path.exists(filename)