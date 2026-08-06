import pytest
from src_1022 import task_func
import binascii
import hashlib

def test_task_func_with_verify_hash():
    input_string = "Hello, world!"
    verify_hash = hashlib.sha256(input_string.encode()).hexdigest()
    result = task_func(input_string, verify_hash)
    assert result == verify_hash

def test_task_func_without_verify_hash():
    input_string = "Hello, world!"
    result = task_func(input_string)
    hashed_bytes = hashlib.sha256(input_string.encode()).digest()
    hex_encoded_hash = binascii.hexlify(hashed_bytes).decode()
    assert result == hex_encoded_hash

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_with_invalid_verify_hash():
    input_string = "Hello, world!"
    verify_hash = "invalid_hash"
    with pytest.raises(TypeError):
        task_func(input_string, verify_hash)