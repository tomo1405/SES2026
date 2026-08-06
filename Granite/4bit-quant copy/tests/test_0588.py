import pytest
from src_0588 import task_func

def test_task_func():
    file_path = 'test_file.txt'
    pub_key, encrypted_file, encrypted_key_file = task_func(file_path)

    assert pub_key  # Replace with the expected value
    assert encrypted_file == file_path + '.encrypted'
    assert encrypted_key_file == 'aes_key.encrypted'