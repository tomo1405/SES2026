import pytest
from src_0587 import task_func
import os
import rsa
from cryptography.fernet import Fernet
from base64 import b64decode

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'wb') as f:
        f.write(b"Hello, World!")
    return file_path

def test_task_func(temp_file):
    pub_key, encrypted_file, encrypted_key_file = task_func(str(temp_file))
    
    # Check if the encrypted file exists
    assert os.path.exists(encrypted_file)
    
    # Check if the encrypted key file exists
    assert os.path.exists(encrypted_key_file)
    
    # Read the encrypted file
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Read the encrypted key file
    with open(encrypted_key_file, 'rb') as f:
        encrypted_fernet_key_b64 = f.read()
        encrypted_fernet_key = b64decode(encrypted_fernet_key_b64)
    
    # Decrypt the fernet key using the public key
    fernet_key = rsa.decrypt(encrypted_fernet_key, pub_key)
    fernet = Fernet(fernet_key)
    
    # Decrypt the data using the fernet key
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Check if the decrypted data matches the original data
    with open(temp_file, 'rb') as f:
        original_data = f.read()
    
    assert decrypted_data == original_data

def test_task_func_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.txt")