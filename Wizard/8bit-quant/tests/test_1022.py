python
import binascii
import hashlib
import pytest

def task_func(input_string, verify_hash=None):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    if verify_hash is not None and not isinstance(verify_hash, str):
        raise TypeError("verify_hash must be a string or None")

    hashed_bytes = hashlib.sha256(input_string.encode()).digest()
    hex_encoded_hash = binascii.hexlify(hashed_bytes).decode()

    if verify_hash is not None:
        return hex_encoded_hash == verify_hash

    return hex_encoded_hash

def test_task_func_valid_input():
    assert task_func("hello world") == "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_verify_hash():
    assert task_func("hello world", "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e") == True
    assert task_func("hello world", "invalid hash") == False