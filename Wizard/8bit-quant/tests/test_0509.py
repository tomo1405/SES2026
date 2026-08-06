python
import hashlib
import io
import os
import pytest

def task_func(file_path1, file_path2):
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("File not found! Please specify a valid filepath")

    with io.open(file_path1, 'rb') as file1, io.open(file_path2, 'rb') as file2:
        file1_hash = hashlib.md5(file1.read()).hexdigest()
        file2_hash = hashlib.md5(file2.read()).hexdigest()

    return file1_hash == file2_hash

def test_task_func():
    # Test case 1: Same file
    assert task_func('test_file.txt', 'test_file.txt') == True

    # Test case 2: Different files
    with open('test_file1.txt', 'w') as f:
        f.write('Hello, world!')
    with open('test_file2.txt', 'w') as f:
        f.write('Hello, world!')
    assert task_func('test_file1.txt', 'test_file2.txt') == False

    # Test case 3: File not found
    with pytest.raises(FileNotFoundError):
        task_func('test_file1.txt', 'test_file3.txt')