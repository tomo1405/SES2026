import pytest
from src_0584 import task_func
import os
from Crypto.Cipher import AES
from base64 import b64decode

def test_task_func():
    pub_key, filename, password, nonce = task_func()

    # Check that the public key is an instance of rsa.PublicKey
    assert isinstance(pub_key, rsa.PublicKey)

    # Check that the filename is a string and has the correct format
    assert isinstance(filename, str)
    assert filename.startswith('private_key_')
    assert filename.endswith('.txt')

    # Check that the password is 16 bytes long
    assert isinstance(password, bytes)
    assert len(password) == 16

    # Check that the nonce is appropriate for AES.MODE_EAX
    assert isinstance(nonce, bytes)
    assert len(nonce) == AES.block_size

    # Read the encrypted private key from the file
    with open(filename, 'r') as f:
        encrypted_priv_key_b64 = f.read()
    encrypted_priv_key = b64decode(encrypted_priv_key_b64)

    # Decrypt the private key using the password and nonce
    cipher = AES.new(password, AES.MODE_EAX, nonce=nonce)
    decrypted_priv_key = cipher.decrypt(encrypted_priv_key)

    # Load the decrypted private key and check it's an instance of rsa.PrivateKey
    priv_key = rsa.PrivateKey.load_pkcs1(decrypted_priv_key)
    assert isinstance(priv_key, rsa.PrivateKey)

    # Clean up the created file
    os.remove(filename)