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
    source_directory = 'source_directory'
    destination_directory = 'destination_directory'
    file_pattern = '*.txt'
    moved_files = task_func(source_directory, destination_directory, file_pattern)
    assert moved_files == ['file1.txt', 'file2.txt']