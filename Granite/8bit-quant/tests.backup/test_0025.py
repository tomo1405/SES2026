import base64
import hashlib
import os
import pytest
from src_0025 import task_func

def test_task_func_with_valid_password():
    password = "password"
    salt, hashed_password = task_func(password)
    assert isinstance(salt, bytes)
    assert isinstance(hashed_password, bytes)
    assert len(salt) == 32
    assert len(hashed_password) == 48

def test_task_func_with_empty_password():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_with_long_password():
    password = "a" * 10000
    salt, hashed_password = task_func(password)
    assert isinstance(salt, bytes)
    assert isinstance(hashed_password, bytes)
    assert len(salt) == 32
    assert len(hashed_password) == 48