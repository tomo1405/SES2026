import pytest
from src_0587 import task_func

def test_task_func():
    # Test that the function returns the correct values
    pub_key, encrypted_file, encrypted_key_file = task_func('test_file.txt')
    assert pub_key == 'test_file.txt.pub'
    assert encrypted_file == 'test_file.txt.encrypted'
    assert encrypted_key_file == 'fernet_key.encrypted'

    # Test that the function encrypts the file correctly
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    assert encrypted_data != b'test_file.txt'

    # Test that the function encrypts the Fernet key correctly
    with open(encrypted_key_file, 'rb') as f:
        encrypted_fernet_key = f.read()
    assert encrypted_fernet_key != b'fernet_key'

    # Test that the function returns the correct public key
    assert pub_key == 'test_file.txt.pub'