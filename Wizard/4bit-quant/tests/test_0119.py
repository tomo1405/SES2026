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
    directory = 'test_dir'
    backup_directory = 'backup_dir'

    # create test directory and files
    os.makedirs(directory)
    with open(os.path.join(directory, 'file1.json'), 'w') as f:
        f.write('test')
    with open(os.path.join(directory, 'file2.txt'), 'w') as f:
        f.write('test')

    # call task_func and assert result
    result = task_func(directory, backup_directory)
    assert result == [os.path.join(backup_directory, 'file1.json')]

    # assert backup directory was created
    assert os.path.exists(backup_directory)

    # assert files were copied
    assert os.path.exists(os.path.join(backup_directory, 'file1.json'))
    assert not os.path.exists(os.path.join(backup_directory, 'file2.txt'))

    # remove test directory and backup directory
    shutil.rmtree(directory)
    shutil.rmtree(backup_directory)