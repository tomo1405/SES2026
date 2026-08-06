import hashlib
import rsa
import base64
from src_0505 import task_func
import pytest

def test_task_func():
    file_path = 'path/to/test/file'
    with open(file_path, 'rb') as f:
        content = f.read()

    hash_output = hashlib.sha256(content).digest()

    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
    signature = rsa.sign(hash_output, private_key, 'SHA-256')

    expected_output = base64.b64encode(signature).decode('utf-8')

    actual_output = task_func(file_path)

    assert actual_output == expected_output