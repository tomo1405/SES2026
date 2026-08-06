import pytest
from src_0584 import task_func
import os
from Crypto.Cipher import AES
from base64 import b64decode

def test_task_func():
    pub_key, filename, password, nonce = task_func()

    # Check if the public key is an instance of rsa.PublicKey
    assert isinstance(pub_key, rsa.PublicKey)

    # Check if the filename exists and is a file
    assert os.path.isfile(filename)

    # Read the encrypted private key from the file
    with open(filename, 'r') as f:
        encrypted_priv_key_str = f.read()

    # Decode the base64 encoded string
    encrypted_priv_key = b64decode(encrypted_priv_key_str)

    # Decrypt the private key using the provided password and nonce
    cipher = AES.new(password, AES.MODE_EAX, nonce=nonce)
    decrypted_priv_key = cipher.decrypt(encrypted_priv_key)

    # Load the decrypted private key into an RSA PrivateKey object
    priv_key = rsa.PrivateKey.load_pkcs1(decrypted_priv_key)

    # Check if the decrypted private key is an instance of rsa.PrivateKey
    assert isinstance(priv_key, rsa.PrivateKey)

    # Clean up the created file
    os.remove(filename)