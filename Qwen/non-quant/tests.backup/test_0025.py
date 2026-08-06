import pytest
from src_0025 import task_func

def test_task_func_with_valid_password():
    password = "secure_password"
    salt, hashed_password = task_func(password)
    assert isinstance(salt, bytes)
    assert isinstance(hashed_password, bytes)

def test_task_func_with_empty_password():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_with_salt_length():
    password = "secure_password"
    salt_length = 64
    salt, hashed_password = task_func(password, SALT_LENGTH=salt_length)
    assert len(base64.b64decode(salt)) == salt_length
    assert isinstance(salt, bytes)
    assert isinstance(hashed_password, bytes)

def test_task_func_consistency():
    password = "secure_password"
    salt1, hashed_password1 = task_func(password)
    salt2, hashed_password2 = task_func(password)
    assert salt1 != salt2
    assert hashed_password1 != hashed_password2