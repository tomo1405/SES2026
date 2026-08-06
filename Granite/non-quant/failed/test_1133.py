import os
import hashlib
import base64
from src_1133 import task_func
import pytest

def test_task_func():
    password = "password"
    result = task_func(password)
    assert isinstance(result, str)
    assert result.startswith("ME")

def test_task_func_with_salt_length():
    password = "password"
    salt_length = 16
    result = task_func(password, SALT_LENGTH=salt_length)
    assert len(result) == 44

def test_task_func_with_invalid_salt_length():
    password = "password"
    salt_length = -1
    with pytest.raises(ValueError):
        task_func(password, SALT_LENGTH=salt_length)

def test_task_func_with_multiple_calls():
    password = "password"
    salt_length = 16
    result1 = task_func(password, SALT_LENGTH=salt_length)
    result2 = task_func(password, SALT_LENGTH=salt_length)
    assert result1 != result2