import os

import pytest
from src_0588 import task_func


def test_task_func():
    file_path = 'test_file.txt'
    pub_key, encrypted_file, encrypted_key_file = task_func(file_path)
    assert pub_key is not None
    assert encrypted_file is not None
    assert encrypted_key_file is not None
    assert os.path.exists(encrypted_file)
    assert os.path.exists(encrypted_key_file)
    assert os.path.getsize(encrypted_file) > 0
    assert os.path.getsize(encrypted_key_file) > 0

def test_task_func_invalid_file():
    file_path = 'invalid_file.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

def test_task_func_invalid_key():
    file_path = 'test_file.txt'
    with pytest.raises(ValueError):
        task_func(file_path, key='invalid_key')