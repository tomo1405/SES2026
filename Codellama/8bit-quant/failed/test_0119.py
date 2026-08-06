import pytest
from src_0119 import task_func

def test_task_func():
    directory = 'test_directory'
    backup_directory = 'test_backup_directory'
    copied_files = task_func(directory, backup_directory)
    assert len(copied_files) == 2
    assert os.path.exists(copied_files[0])
    assert os.path.exists(copied_files[1])
    assert os.path.join(backup_directory, 'file1.json') in copied_files
    assert os.path.join(backup_directory, 'file2.json') in copied_files