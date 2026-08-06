python
import ctypes
import hashlib
import binascii
import pytest

def task_func(filepath):
    lib = ctypes.CDLL(filepath)

    with open(filepath, 'rb') as f:
        data = f.read()

    md5_hash = hashlib.md5(data).digest()
    print(f'MD5 Hash: {binascii.hexlify(md5_hash).decode()}')

    sha256_hash = hashlib.sha256(data).digest()
    print(f'SHA256 Hash: {binascii.hexlify(sha256_hash).decode()}')

    return lib._name

def test_task_func():
    filepath = 'libtest.so'
    assert task_func(filepath) == 'libtest.so'