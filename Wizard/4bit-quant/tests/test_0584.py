python
import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import pytest

def task_func():
    (pub_key, priv_key) = rsa.newkeys(512)
    password = get_random_bytes(16)

    cipher = AES.new(password, AES.MODE_EAX)
    nonce = cipher.nonce
    priv_key_encrypted, tag = cipher.encrypt_and_digest(priv_key.save_pkcs1())

    priv_key_encrypted = b64encode(priv_key_encrypted).decode('utf-8')

    filename = f'private_key_{os.urandom(8).hex()}.txt'
    with open(filename, 'w') as f:
        f.write(priv_key_encrypted)

    return pub_key, filename, password, nonce

def test_task_func():
    pub_key, filename, password, nonce = task_func()
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(filename, str)
    assert isinstance(password, bytes)
    assert isinstance(nonce, bytes)
    assert os.path.exists(filename)
    os.remove(filename)