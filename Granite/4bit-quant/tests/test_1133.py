import os
import hashlib
import base64
import pytest

from src_1133 import task_func

def test_task_func():
    password = "password"
    hashed_password = task_func(password)
    assert isinstance(hashed_password, str)
    assert len(hashed_password) == 44  # base64 encoded SHA256 hash has 44 characters
    assert hashed_password.startswith("ME")  # check the PREFIX is included in the result

def test_task_func_invalid_salt_length():
    password = "password"
    with pytest.raises(ValueError):
        task_func(password, SALT_LENGTH=-1)