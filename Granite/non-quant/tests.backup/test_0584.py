import pytest
from src_0584 import task_func

def test_task_func():
    pub_key, filename, password, nonce = task_func()
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(filename, str)
    assert isinstance(password, bytes)
    assert isinstance(nonce, bytes)