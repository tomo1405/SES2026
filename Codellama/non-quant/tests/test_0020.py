import os
import zipfile

import pytest
from src_0020 import task_func


def test_task_func_valid_directory():
    directory = 'test_directory'
    os.makedirs(directory, exist_ok=True)
    file1 = os.path.join(directory, 'file1.txt')
    file2 = os.path.join(directory, 'file2.txt')
    with open(file1, 'w') as f:
        f.write('file1')
    with open(file2, 'w') as f:
        f.write('file2')
    zip_file_path = task_func(directory)
    assert os.path.exists(zip_file_path)
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        assert zipf.namelist() == ['file1.txt', 'file2.txt']
    os.remove(zip_file_path)

def test_task_func_invalid_directory():
    directory = 'invalid_directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_empty_directory():
    directory = 'empty_directory'
    os.makedirs(directory, exist_ok=True)
    zip_file_path = task_func(directory)
    assert zip_file_path is None
    os.remove(zip_file_path)