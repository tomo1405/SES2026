import pytest
from src_0587 import task_func

def test_task_func():
    file_path = 'test_file.txt'
    pub_key, encrypted_file, encrypted_key_file = task_func(file_path)

    assert pub_key is not None
    assert encrypted_file is not None
    assert encrypted_key_file is not None

    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
        assert encrypted_data is not None

    with open(encrypted_key_file, 'rb') as f:
        encrypted_fernet_key = f.read()
        assert encrypted_fernet_key is not None

    assert rsa.decrypt(encrypted_fernet_key, priv_key) == fernet_key