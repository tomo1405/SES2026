import pytest
from src_0760 import task_func

def test_task_func():
    source_directory = 'path/to/source/directory'
    destination_directory = 'path/to/destination/directory'
    file_pattern = '*.txt'
    moved_files = task_func(source_directory, destination_directory, file_pattern)
    assert moved_files == ['file1.txt', 'file2.txt', 'file3.txt']