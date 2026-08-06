import pytest
from src_0584 import task_func

def test_task_func():
    pub_key, filename, password, nonce = task_func()
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(filename, str)
    assert isinstance(password, bytes)
    assert isinstance(nonce, bytes)

    with open(filename, 'r') as f:
        priv_key_encrypted = f.read()
    priv_key_encrypted = b64decode(priv_key_encrypted)
    cipher = AES.new(password, AES.MODE_EAX, nonce=nonce)
    priv_key_decrypted = cipher.decrypt(priv_key_encrypted)
    priv_key_decrypted = rsa.PrivateKey.load_pkcs1(priv_key_decrypted)
    assert priv_key_decrypted == priv_key