import base64

import pytest
from cryptography.hazmat.primitives.asymmetric import rsa
from src_0535 import task_func


@pytest.fixture
def private_key():
    # Generate a private key for testing purposes
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return private_key

@pytest.fixture
def public_key(private_key):
    # Generate the corresponding public key
    public_key = private_key.public_key()
    return public_key

def test_task_func_with_valid_input(private_key):
    num = "123"
    from_base = 10
    to_base = 16
    alphabet = "0123456789abcdef"
    
    result = task_func(num, from_base, to_base, private_key, alphabet)
    
    # Verify that the result is a base64 encoded string
    assert isinstance(result, str)
    assert base64.b64decode(result) is not None

def test_task_func_with_invalid_base(private_key):
    num = "123"
    from_base = 1
    to_base = 16
    alphabet = "0123456789abcdef"
    
    with pytest.raises(ValueError):
        task_func(num, from_base, to_base, private_key, alphabet)

def test_task_func_with_empty_alphabet(private_key):
    num = "123"
    from_base = 10
    to_base = 16
    alphabet = ""
    
    with pytest.raises(IndexError):
        task_func(num, from_base, to_base, private_key, alphabet)

def test_task_func_with_large_number(private_key):
    num = "12345678901234567890"
    from_base = 10
    to_base = 16
    alphabet = "0123456789abcdef"
    
    result = task_func(num, from_base, to_base, private_key, alphabet)
    
    # Verify that the result is a base64 encoded string
    assert isinstance(result, str)
    assert base64.b64decode(result) is not None

def test_task_func_with_small_number(private_key):
    num = "0"
    from_base = 10
    to_base = 16
    alphabet = "0123456789abcdef"
    
    result = task_func(num, from_base, to_base, private_key, alphabet)
    
    # Verify that the result is a base64 encoded string
    assert isinstance(result, str)
    assert base64.b64decode(result) is not None