python
import base64
import hashlib
import hmac
import binascii
import pytest

def task_func(s, signature, secret_key):
    decoded_msg = base64.b64decode(s).decode()
    computed_signature = hmac.new(secret_key.encode(), decoded_msg.encode(), hashlib.sha1)
    return binascii.hexlify(computed_signature.digest()).decode() == signature

def test_task_func():
    # Test case 1
    s = "SGVsbG8gV29ybGQh"
    signature = "1c7f1d1d5d5d5d1c1c1c1c1c1c1c1c1c1c1c1c1c"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == True
    
    # Test case 2
    s = "Hello World!"
    signature = "1c7f1d1d5d5d5d1c1c1c1c1c1c1c1c1c1c1c1c1c"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == True
    
    # Test case 3
    s = "Hello World!"
    signature = "1c7f1d1d5d5d5d1c1c1c1c1c1c1c1c1c1c1c1c1d"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == False
    
    # Test case 4
    s = "Hello World!"
    signature = "1c7f1d1d5d5d5d1c1c1c1c1c1c1c1c1c1c1c1c1c"
    secret_key = "wrong_secret"
    assert task_func(s, signature, secret_key) == False