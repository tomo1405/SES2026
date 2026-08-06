import glob
import os

from src_0786 import task_func


def test_task_func_no_files():
    pattern = '*.txt'
    assert task_func(pattern) == "No files found matching the pattern."

def test_task_func_one_file():
    pattern = 'test_file.txt'
    assert task_func(pattern) == 'archive.tar.gz'

def test_task_func_multiple_files():
    pattern = 'test_file*.txt'
    assert task_func(pattern) == 'archive.tar.gz'

def test_task_func_archive_exists():
    pattern = 'test_file*.txt'
    archive_file = 'archive.tar.gz'
    if os.path.exists(archive_file):
        os.remove(archive_file)
    assert task_func(pattern) == 'archive.tar.gz'
    assert os.path.exists(archive_file)

def test_task_func_delete_files():
    pattern = 'test_file*.txt'
    file_list = glob.glob(pattern)
    assert task_func(pattern) == 'archive.tar.gz'
    for file in file_list:
        assert not os.path.exists(file)