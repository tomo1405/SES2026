python
import hashlib
import rsa
import base64
import pytest

from src_0505 import task_func

def test_task_func():
    with open('test_file.txt', 'w') as f:
        f.write('test')

    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())

    signature = task_func('test_file.txt')

    assert signature == 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

    with open('test_file.txt', 'w') as f:
        f.write('test2')

    with pytest.raises(ValueError):
        task_func('test_file.txt')