python
import os
import shutil
import pytest

def task_func(directory, backup_directory):
    copied_files = []

    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            src = os.path.join(directory, filename)
            dst = os.path.join(backup_directory, filename)
            shutil.copy(src, dst)
            copied_files.append(dst)

    return copied_files

def test_task_func():
    directory = 'data'
    backup_directory = 'backup'
    expected_files = [os.path.join(backup_directory, 'file1.json'), os.path.join(backup_directory, 'file2.json')]

    # Test copying files
    copied_files = task_func(directory, backup_directory)
    assert len(copied_files) == len(expected_files)
    assert set(copied_files) == set(expected_files)

    # Test backup directory creation
    assert os.path.exists(backup_directory)

    # Test copying non-json files
    os.makedirs(os.path.join(directory, 'subdir'))
    with open(os.path.join(directory, 'subdir', 'file3.txt'), 'w') as f:
        f.write('test')
    copied_files = task_func(directory, backup_directory)
    assert len(copied_files) == len(expected_files)
    assert set(copied_files) == set(expected_files)

    # Test copying files to non-existent directory
    backup_directory = 'nonexistent'
    copied_files = task_func(directory, backup_directory)
    assert len(copied_files) == 0
    assert not os.path.exists(backup_directory)