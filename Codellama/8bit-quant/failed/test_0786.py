import pytest
from src_0786 import task_func

def test_task_func_no_files():
    pattern = '*.txt'
    assert task_func(pattern) == "No files found matching the pattern."

def test_task_func_one_file():
    pattern = '*.txt'
    file_list = ['file1.txt']
    assert task_func(pattern) == 'archive.tar.gz'

def test_task_func_multiple_files():
    pattern = '*.txt'
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    assert task_func(pattern) == 'archive.tar.gz'

def test_task_func_archive_file_exists():
    pattern = '*.txt'
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    archive_file_base = os.path.join(ARCHIVE_DIR, 'archive')
    archive_file = archive_file_base + '.tar.gz'
    counter = 1
    while os.path.exists(archive_file):
        archive_file = archive_file_base + f"_{counter}.tar.gz"
        counter += 1
    assert task_func(pattern) == archive_file

def test_task_func_delete_files():
    pattern = '*.txt'
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    assert task_func(pattern) == 'archive.tar.gz'
    for file in file_list:
        assert not os.path.exists(file)