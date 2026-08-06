import base64
import hashlib
import os
import pytest
from src_0025 import task_func

def test_task_func():
    password = "test_password"
    salt, hashed_password = task_func(password)
    assert isinstance(salt, bytes)
    assert isinstance(hashed_password, bytes)
    assert len(salt) == 32
    assert len(hashed_password) == 48
    with pytest.raises(ValueError):
        task_func("")