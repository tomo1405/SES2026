import os

import pytest
from src_0264 import task_func


def test_task_func_valid_input():
    my_path = 'path/to/files'
    days_old = 30
    archive_dir = task_func(my_path, days_old)
    assert os.path.isdir(archive_dir)
    assert os.path.isfile(os.path.join(archive_dir, 'file1.txt'))
    assert os.path.isfile(os.path.join(archive_dir, 'file2.csv'))
    assert os.path.isfile(os.path.join(archive_dir, 'file3.xlsx'))
    assert os.path.isfile(os.path.join(archive_dir, 'file4.docx'))
    assert os.path.isfile(os.path.join(archive_dir, 'file5.pdf'))

def test_task_func_invalid_input():
    my_path = 'path/to/files'
    days_old = 0
    with pytest.raises(ValueError):
        task_func(my_path, days_old)

def test_task_func_invalid_path():
    my_path = 'path/to/invalid/files'
    days_old = 30
    with pytest.raises(FileNotFoundError):
        task_func(my_path, days_old)