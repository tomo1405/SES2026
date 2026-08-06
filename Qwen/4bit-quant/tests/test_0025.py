import pytest
from src_0025 import task_func

def test_task_func_valid_password():
    password = "secure_password"
    salt, hashed_password = task_func(password)
    assert isinstance(salt, bytes)
    assert isinstance(hashed_password, bytes)
    assert len(salt) == 32
    assert len(hashed_password) > 0

def test_task_func_empty_password():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_salt_length():
    password = "another_secure_password"
    salt, _ = task_func(password, SALT_LENGTH=16)
    assert len(salt) == 16

def test_task_func_hashed_password_length():
    password = "yet_another_secure_password"
    _, hashed_password = task_func(password)
    # Length of the hashed password in base64 should be greater than 0
    assert len(hashed_password) > 0

def test_task_func_repeated_calls_different_results():
    password = "password123"
    result1 = task_func(password)
    result2 = task_func(password)
    assert result1 != result2, "Salt and/or hashed password should be different for repeated calls"