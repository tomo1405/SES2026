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
    s = "d29vZ2xlYXN0ZXI="
    signature = "1b0052150791f50f8c732991451202b521f5d6c0"
    secret_key = "my_secret_key"
    
    result = task_func(s, signature, secret_key)
    assert result == True