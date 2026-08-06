python
import hashlib
import re
import pytest

def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str)
    hashed_str = hashlib.sha256(cleaned_str.encode()).hexdigest()

    return hashed_str

def test_task_func():
    assert task_func('Hello, World!') == 'a1d0c9e8c98d5c6e1c44e0c5f99567e7e45c7f3d04c0461c6b8d5d949e0e22c3'
    assert task_func('12345') == 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
    assert task_func('abc') == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'