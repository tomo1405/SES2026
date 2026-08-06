import os

import rsa
from src_0588 import task_func


def test_task_func():
    file_path = 'test_file.txt'
    pub_key, encrypted_file, encrypted_key_file = task_func(file_path)

    assert os.path.exists(encrypted_file)
    assert os.path.exists(encrypted_key_file)

    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()

    assert len(encrypted_data) > 0

    with open(encrypted_key_file, 'rb') as f:
        encrypted_aes_key = f.read()

    assert len(encrypted_aes_key) > 0

    assert rsa.verify(encrypted_aes_key, aes_key, pub_key)