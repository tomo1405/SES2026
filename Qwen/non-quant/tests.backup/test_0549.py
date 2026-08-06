import pytest
from src_0549 import task_func
import random
import string
import base64
import zlib

def test_task_func_default_length():
    result = task_func()
    assert isinstance(result, str)
    assert len(base64.b64decode(result)) > 0

def test_task_func_custom_length():
    length = 200
    result = task_func(length)
    assert isinstance(result, str)
    decoded_result = base64.b64decode(result)
    decompressed_result = zlib.decompress(decoded_result)
    assert len(decompressed_result.decode('utf-8')) == length

def test_task_func_randomness():
    result1 = task_func()
    result2 = task_func()
    assert result1 != result2

def test_task_func_valid_characters():
    result = task_func()
    decoded_result = base64.b64decode(result)
    decompressed_result = zlib.decompress(decoded_result)
    assert all(c in string.ascii_uppercase + string.digits for c in decompressed_result.decode('utf-8'))

def test_task_func_empty_string():
    with pytest.raises(ValueError):
        task_func(0)