import pytest
from src_0585 import task_func

def test_task_func_valid_url():
    url = "https://www.example.com"
    pub_key, signed_hash, hash_value = task_func(url)
    assert isinstance(pub_key, rsa.PublicKey)
    assert isinstance(signed_hash, str)
    assert isinstance(hash_value, bytes)

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_invalid_hash():
    url = "https://www.example.com"
    with pytest.raises(rsa.pkcs1.VerificationError):
        task_func(url)