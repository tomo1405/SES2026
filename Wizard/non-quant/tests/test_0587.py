python
import rsa
import pytest
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    (pub_key, priv_key) = rsa.newkeys(512)
    fernet_key = Fernet.generate_key()
    fernet = Fernet(fernet_key)

    with open(file_path, 'rb') as f:
        data = f.read()
        encrypted_data = fernet.encrypt(data)

    encrypted_file = file_path + '.encrypted'
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_data)

    encrypted_fernet_key = rsa.encrypt(fernet_key, pub_key)
    encrypted_key_file = 'fernet_key.encrypted'
    with open(encrypted_key_file, 'wb') as f:
        f.write(b64encode(encrypted_fernet_key))

    return pub_key, encrypted_file, encrypted_key_file

def test_task_func():
    pub_key, encrypted_file, encrypted_key_file = task_func('test.txt')
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(encrypted_file, str)
    assert isinstance(encrypted_key_file, str)
    assert encrypted_file.endswith('.encrypted')
    assert encrypted_key_file.endswith('.encrypted')
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    with open(encrypted_key_file, 'rb') as f:
        encrypted_fernet_key = f.read()
    decrypted_fernet_key = rsa.decrypt(encrypted_fernet_key, priv_key)
    fernet = Fernet(decrypted_fernet_key)
    with open('test.txt', 'rb') as f:
        data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    assert data == decrypted_data