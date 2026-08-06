import pytest
from src_0314 import task_func


def test_task_func():
    directory = 'test_directory'
    moved_files = task_func(directory)
    assert moved_files == {'subdirectory1': ['file1_20220314123456.txt', 'file2_20220314123456.txt'],
                          'subdirectory2': ['file3_20220314123456.txt', 'file4_20220314123456.txt']}