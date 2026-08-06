import binascii
import ctypes
import hashlib

from src_0566 import task_func


def test_task_func():
    filepath = 'path/to/file'
    lib = ctypes.CDLL(filepath)

    with open(filepath, 'rb') as f:
        data = f.read()

    md5_hash = hashlib.md5(data).digest()
    assert md5_hash == binascii.hexlify(md5_hash).decode()

    sha256_hash = hashlib.sha256(data).digest()
    assert sha256_hash == binascii.hexlify(sha256_hash).decode()

    assert task_func(filepath) == lib._name