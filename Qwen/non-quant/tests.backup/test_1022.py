import pytest
from src_1022 import task_func

def test_task_func_input_not_string():
    with pytest.raises(TypeError, match="Input must be a string"):
        task_func(123)

def test_task_func_verify_hash_not_string():
    with pytest.raises(TypeError, match="verify_hash must be a string or None"):
        task_func("test", 123)

def test_task_func_no_verify_hash():
    result = task_func("test")
    assert isinstance(result, str)
    assert len(result) == 64

def test_task_func_with_verify_hash_match():
    input_string = "test"
    expected_hash = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    assert task_func(input_string, expected_hash) is True

def test_task_func_with_verify_hash_mismatch():
    input_string = "test"
    incorrect_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    assert task_func(input_string, incorrect_hash) is False

def test_task_func_empty_string():
    result = task_func("")
    assert result == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"