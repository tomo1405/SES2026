import pytest
from src_0505 import task_func
import os
import hashlib
import rsa
import base64

# Mocking the file operations and RSA signing process
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

def mock_open(filename, mode):
    if filename == 'test_file.txt':
        return MockFile(b'Test file content')
    elif filename == 'private.pem':
        # Generate a dummy private key for testing
        (public_key, private_key) = rsa.newkeys(512)
        return MockFile(private_key.save_pkcs1())

def test_task_func(mocker):
    # Mock the open function to return our mock files
    mocker.patch('builtins.open', side_effect=mock_open)

    # Call the function with a test file path
    result = task_func('test_file.txt')

    # Verify that the result is a base64 encoded string
    assert isinstance(result, str)
    assert base64.b64decode(result)

    # Verify the signature by checking if it can be verified with the public key
    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
    public_key = private_key.publickey()

    # Calculate the expected hash of the file content
    expected_hash = hashlib.sha256(b'Test file content').digest()

    try:
        # Attempt to verify the signature
        rsa.verify(base64.b64decode(result), public_key, expected_hash)
        assert True
    except rsa.VerificationError:
        assert False

# Clean up any temporary files created during testing
@pytest.fixture(autouse=True)
def cleanup():
    yield
    if os.path.exists('test_file.txt'):
        os.remove('test_file.txt')
    if os.path.exists('private.pem'):
        os.remove('private.pem')