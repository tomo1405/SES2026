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
    s = "d29ya3N1ZXI="
    signature = "51d3b2e19f0e7c8e1f1e0e9c0e7c8e1f1e0e9c0e7c8e1f1e0e9c0e7c8e1f1e0e"
    secret_key = "secret"

    assert task_func(s, signature, secret_key) == True