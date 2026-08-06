import pytest
from src_1022 import task_func

def test_task_func_input_string_not_str():
    with pytest.raises(TypeError, match="Input must be a string"):
        task_func(123)

def test_task_func_verify_hash_not_str():
    with pytest.raises(TypeError, match="verify_hash must be a string or None"):
        task_func("test", 123)

def test_task_func_no_verify_hash():
    result = task_func("test")
    assert isinstance(result, str)
    assert len(result) == 64  # SHA-256 hash length in hexadecimal

def test_task_func_verify_hash_match():
    input_string = "test"
    correct_hash = task_func(input_string)  # Get the correct hash first
    assert task_func(input_string, correct_hash) is True

def test_task_func_verify_hash_mismatch():
    input_string = "test"
    incorrect_hash = "wronghash"
    assert task_func(input_string, incorrect_hash) is False

def test_task_func_empty_string():
    result = task_func("")
    assert result == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

def test_task_func_unicode_string():
    result = task_func("你好")
    assert isinstance(result, str)
    assert len(result) == 64  # SHA-256 hash length in hexadecimal