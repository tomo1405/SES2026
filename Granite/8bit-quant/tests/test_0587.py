import pytest
from src_0587 import task_func

def test_task_func():
    file_path = 'test_file.txt'
    pub_key, encrypted_file, encrypted_key_file = task_func(file_path)

    assert pub_key  # Check if pub_key is not None
    assert encrypted_file == file_path + '.encrypted'  # Check if encrypted_file has the correct file name
    assert encrypted_key_file == 'fernet_key.encrypted'  # Check if encrypted_key_file has the correct file name