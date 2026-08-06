import pytest
from src_0119 import task_func

def test_task_func():
    directory = 'path/to/directory'
    backup_directory = 'path/to/backup_directory'
    copied_files = task_func(directory, backup_directory)
    assert len(copied_files) == 2
    assert copied_files[0] == 'path/to/backup_directory/file1.json'
    assert copied_files[1] == 'path/to/backup_directory/file2.json'