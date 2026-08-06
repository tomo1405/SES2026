import pytest
from src_0505 import task_func
import hashlib
import rsa
import base64
import os

# Mocking the file reading and key loading to avoid actual file operations
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

def test_task_func(mocker):
    # Mock the file reading
    mock_content = b"some file content"
    mocker.patch('builtins.open', side_effect=[
        MockFile(mock_content),  # First open is for the file_path
        MockFile(rsa.PrivateKey.save_pkcs1(rsa.newkeys(512)[1]))  # Second open is for 'private.pem'
    ])

    # Expected hash output
    expected_hash = hashlib.sha256(mock_content).digest()

    # Expected signature (using the mocked private key)
    private_key = rsa.PrivateKey.load_pkcs1(rsa.PrivateKey.save_pkcs1(rsa.newkeys(512)[1]))
    expected_signature = rsa.sign(expected_hash, private_key, 'SHA-256')
    expected_b64_signature = base64.b64encode(expected_signature).decode('utf-8')

    # Call the function
    result = task_func("dummy_path")

    # Assert the result
    assert result == expected_b64_signature