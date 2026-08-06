import pytest
from src_0588 import task_func
import os
import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64decode

def test_task_func(tmpdir):
    # Create a temporary file and write some data to it
    temp_file = tmpdir.join('testfile.txt')
    temp_file.write_binary(b'This is a test file.')

    # Call the task_func
    pub_key, encrypted_file, encrypted_key_file = task_func(str(temp_file))

    # Check that the encrypted file exists
    assert os.path.exists(encrypted_file)

    # Check that the encrypted key file exists
    assert os.path.exists(encrypted_key_file)

    # Read the encrypted AES key from the file
    with open(encrypted_key_file, 'rb') as f:
        encrypted_aes_key = b64decode(f.read())

    # Decrypt the AES key using the private key
    aes_key = rsa.decrypt(encrypted_aes_key, rsa.PrivateKey.load_pkcs1(pub_key.save_pkcs1()))

    # Read the encrypted data from the file
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()

    # Decrypt the data using the AES key
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(encrypted_data[:16]), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Check that the decrypted data matches the original data
    assert decrypted_data == b'This is a test file.'