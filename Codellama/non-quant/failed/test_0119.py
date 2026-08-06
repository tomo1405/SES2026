import pytest
from src_0119 import task_func

def test_task_func_copies_json_files():
    directory = 'test_directory'
    backup_directory = 'test_backup_directory'
    expected_copied_files = ['test_directory/file1.json', 'test_directory/file2.json']

    copied_files = task_func(directory, backup_directory)

    assert copied_files == expected_copied_files

def test_task_func_creates_backup_directory_if_not_exists():
    directory = 'test_directory'
    backup_directory = 'test_backup_directory'

    task_func(directory, backup_directory)

    assert os.path.exists(backup_directory)

def test_task_func_does_not_copy_non_json_files():
    directory = 'test_directory'
    backup_directory = 'test_backup_directory'
    expected_copied_files = []

    task_func(directory, backup_directory)

    assert copied_files == expected_copied_files