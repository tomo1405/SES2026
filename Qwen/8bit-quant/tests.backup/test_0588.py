import pytest
from src_0588 import task_func
import os
import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64decode

# Mocking os.urandom to control randomness in tests
class MockRandom:
    def __init__(self, values):
        self.values = values

    def urandom(self, n):
        return self.values.pop(0)

@pytest.fixture
def mock_os_urandom(monkeypatch):
    mock_values = [
        b'\x00' * 32,  # Mock AES key
        b'\x01' * 16   # Mock IV
    ]
    monkeypatch.setattr(os, 'urandom', MockRandom(mock_values).urandom)

@pytest.fixture
def sample_file(tmpdir):
    sample_content = b'This is a sample file content.'
    file_path = tmpdir.join('sample.txt')
    file_path.write_binary(sample_content)
    return str(file_path)

def test_task_func(mock_os_urandom, sample_file):
    pub_key, encrypted_file, encrypted_key_file = task_func(sample_file)

    # Check if the encrypted file exists
    assert os.path.exists(encrypted_file)

    # Check if the encrypted key file exists
    assert os.path.exists(encrypted_key_file)

    # Read the encrypted file content
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()

    # Read the encrypted AES key
    with open(encrypted_key_file, 'rb') as f:
        encrypted_aes_key_b64 = f.read()
        encrypted_aes_key = b64decode(encrypted_aes_key_b64)

    # Decrypt the AES key using the private key
    (pub_key, priv_key) = rsa.newkeys(512)
    decrypted_aes_key = rsa.decrypt(encrypted_aes_key, priv_key)

    # Decrypt the data using the AES key and IV
    iv = b'\x01' * 16  # This is the mocked IV
    cipher = Cipher(algorithms.AES(decrypted_aes_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Check if the decrypted data matches the original content
    with open(sample_file, 'rb') as f:
        original_data = f.read()
    assert decrypted_data == original_data