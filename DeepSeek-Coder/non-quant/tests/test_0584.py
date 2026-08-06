import pytest
from src_0584 import task_func

def test_task_func():
    pub_key, filename, password, nonce = task_func()
    
    assert isinstance(pub_key, type(None)), "Public key should be returned"
    assert isinstance(filename, str), "Filename should be a string"
    assert isinstance(password, bytes), "Password should be bytes"
    assert isinstance(nonce, bytes), "Nonce should be bytes"