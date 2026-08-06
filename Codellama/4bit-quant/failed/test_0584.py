import pytest
from src_0584 import task_func

def test_task_func():
    pub_key, filename, password, nonce = task_func()
    assert isinstance(pub_key, rsa.key.PublicKey)
    assert isinstance(filename, str)
    assert isinstance(password, bytes)
    assert isinstance(nonce, bytes)
    assert len(password) == 16
    assert len(nonce) == 16
    assert os.path.exists(filename)
    with open(filename, 'r') as f:
        priv_key_encrypted = f.read()
    assert isinstance(priv_key_encrypted, str)
    assert priv_key_encrypted.startswith('-----BEGIN RSA PRIVATE KEY-----')
    assert priv_key_encrypted.endswith('-----END RSA PRIVATE KEY-----')
    assert len(priv_key_encrypted) > 0