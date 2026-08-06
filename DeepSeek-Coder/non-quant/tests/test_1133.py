import pytest
from src_1133 import task_func

def test_task_func_basic():
    assert task_func("password123") == "MEpassword123"

def test_task_func_with_prefix():
    assert task_func("password123", "PREFIX") == "PREFIXpassword123"

def test_task_func_with_negative_salt_length():
    with pytest.raises(ValueError):
        task_func("password123", SALT_LENGTH=-1)