import pytest
from src_1022 import task_func

def test_task_func_input_string():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_verify_hash():
    with pytest.raises(TypeError):
        task_func("test", verify_hash=123)

def test_task_func_verify_hash_none():
    assert task_func("test", verify_hash=None) == "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

def test_task_func_verify_hash_match():
    assert task_func("test", verify_hash="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08") == True

def test_task_func_verify_hash_mismatch():
    assert task_func("test", verify_hash="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a09") == False