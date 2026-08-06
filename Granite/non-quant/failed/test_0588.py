import pytest
from src_0588 import task_func

def test_task_func():
    file_path = 'test_file.txt'
    with open(file_path, 'w') as f:
        f.write('Hello, world!')
    pub_key, encrypted_file, encrypted_key_file = task_func(file_path)
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(encrypted_file, str)
    assert isinstance(encrypted_key_file, str)
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    with open(encrypted_key_file, 'rb') as f:
        encrypted_aes_key = f.read()
    assert len(encrypted_data) > 0
    assert len(encrypted_aes_key) > 0