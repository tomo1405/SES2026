import pytest
from src_0584 import task_func
import os
import rsa
from Crypto.Cipher import AES
from base64 import b64decode

def test_task_func():
    pub_key, filename, password, nonce = task_func()

    # Check if the public key is of type rsa.PublicKey
    assert isinstance(pub_key, rsa.PublicKey)

    # Check if the filename is a string and ends with '.txt'
    assert isinstance(filename, str)
    assert filename.endswith('.txt')

    # Check if the password is bytes of length 16
    assert isinstance(password, bytes)
    assert len(password) == 16

    # Check if the nonce is bytes
    assert isinstance(nonce, bytes)

    # Read the encrypted private key from the file
    with open(filename, 'r') as f:
        encrypted_priv_key_base64 = f.read()

    # Decode the base64 encoded private key
    encrypted_priv_key = b64decode(encrypted_priv_key_base64)

    # Decrypt the private key using the password and nonce
    cipher = AES.new(password, AES.MODE_EAX, nonce=nonce)
    decrypted_priv_key = cipher.decrypt(encrypted_priv_key)

    # Load the decrypted private key into an RSA PrivateKey object
    priv_key = rsa.PrivateKey.load_pkcs1(decrypted_priv_key)

    # Check if the decrypted private key is of type rsa.PrivateKey
    assert isinstance(priv_key, rsa.PrivateKey)

    # Clean up the created file
    os.remove(filename)