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
    s = "d29ya3NwYWNlOgogIGJhc2U6CiAgICBpbWFnZTogbG9jYWxob3N0CiAgICB1c2VybmFtZTogcHVibGljCiAgICBwYXNzd29yZDogcGlnbGV0CiAgICB0YWc6IGxhdGVzdAogICAgcGFzc3dvcmQ6IHBhc3N3b3JkCiAgICBkb2NrZXI6IGxhdGVzdAogICAgc2VjdXJlOiBuZXcgc2VjdXJlKCk="
    signature = "5d1e3071e1303700700830370070083037007008303700700830370070083037"
    secret_key = "my_secret_key"

    result = task_func(s, signature, secret_key)
    assert result == True