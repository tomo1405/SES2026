import pytest
from src_1022 import task_func

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func(123)
    with pytest.raises(TypeError):
        task_func("valid_string", 123)

def test_task_func_valid_string_no_verify():
    assert task_func("hello") == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

def test_task_func_valid_string_with_verify_match():
    assert task_func("hello", "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824") is True

def test_task_func_valid_string_with_verify_mismatch():
    assert task_func("hello", "wrong_hash") is False

def test_task_func_empty_string():
    assert task_func("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"