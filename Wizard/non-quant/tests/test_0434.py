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
    s = "VGhpcyBpcyBhIHRlc3Q="
    signature = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
    secret_key = "secret"
    assert task_func(s, signature, secret_key) == True