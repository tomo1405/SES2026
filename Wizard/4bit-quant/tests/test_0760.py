python
import os
import shutil
import fnmatch
import pytest

def task_func(source_directory, destination_directory, file_pattern):
    moved_files = []
    for path, dirs, files in os.walk(source_directory):
        for filename in fnmatch.filter(files, file_pattern):
            shutil.move(os.path.join(path, filename), os.path.join(destination_directory, filename))
            moved_files.append(filename)
    return moved_files

def test_task_func():
    source_directory = 'source_dir'
    destination_directory = 'destination_dir'
    file_pattern = '*.txt'
    os.makedirs(source_directory, exist_ok=True)
    os.makedirs(destination_directory, exist_ok=True)
    with open(os.path.join(source_directory, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(source_directory, 'file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(source_directory, 'file3.txt'), 'w') as f:
        f.write('test')
    moved_files = task_func(source_directory, destination_directory, file_pattern)
    assert moved_files == ['file1.txt', 'file2.txt', 'file3.txt']
    assert os.path.exists(os.path.join(destination_directory, 'file1.txt'))
    assert os.path.exists(os.path.join(destination_directory, 'file2.txt'))
    assert os.path.exists(os.path.join(destination_directory, 'file3.txt'))
    assert not os.path.exists(os.path.join(source_directory, 'file1.txt'))
    assert not os.path.exists(os.path.join(source_directory, 'file2.txt'))
    assert not os.path.exists(os.path.join(source_directory, 'file3.txt'))