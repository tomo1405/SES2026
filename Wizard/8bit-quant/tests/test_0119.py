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
    copied_files = task_func(directory, backup_directory)
    assert len(copied_files) == 2
    assert os.path.exists(os.path.join(backup_directory, 'file1.json'))
    assert os.path.exists(os.path.join(backup_directory, 'file2.json'))