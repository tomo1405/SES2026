import pytest
from src_0505 import task_func
import os
import hashlib
import rsa
import base64

# Mocking the file reading and hashing for testing
def mock_file_read(file_path):
    return b"mock_content"

# Mocking the private key reading
def mock_private_key_read():
    return b"mock_private_key"

# Mocking the file system
def mock_open(file_path, mode):
    if file_path == 'private.pem':
        return mock_private_key_read()
    return open(file_path, mode)

# Patching the file system and hash functions
def test_task_func():
    with patch('builtins.open', mock_open):
        with patch('src_0505.hashlib.sha256', return_value=hashlib.sha256(b"mock_content")):
            with patch('src_0505.rsa.PrivateKey.load_pkcs1', return_value='mock_private_key'):
                result = task_func('mock_file_path')
                assert result == base64.b64encode(b'mock_signature').decode('utf-8')

if __name__ == "__main__":
    test_task_func()