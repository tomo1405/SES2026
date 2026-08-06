import pytest
from src_0587 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary file with some content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file_path = temp_file.name

    # Call the function
    pub_key, encrypted_file, encrypted_key_file = task_func(temp_file_path)

    # Check if the public key is of correct type
    assert isinstance(pub_key, rsa.PublicKey)

    # Check if the encrypted file exists and is not empty
    assert os.path.exists(encrypted_file)
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    assert len(encrypted_data) > 0

    # Check if the encrypted key file exists and is not empty
    assert os.path.exists(encrypted_key_file)
    with open(encrypted_key_file, 'rb') as f:
        encrypted_fernet_key = f.read()
    assert len(encrypted_fernet_key) > 0

    # Clean up temporary files
    os.remove(temp_file_path)
    os.remove(encrypted_file)
    os.remove(encrypted_key_file)