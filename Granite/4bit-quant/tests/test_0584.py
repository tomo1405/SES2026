import pytest
from src_0584 import task_func

def test_task_func():
    pub_key, filename, password, nonce = task_func()
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(filename, str)
    assert isinstance(password, bytes)
    assert isinstance(nonce, bytes)
    assert filename.endswith('.txt')
    assert len(password) == 16
    assert len(nonce) == 16