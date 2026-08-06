import pytest
from src_1133 import task_func

def test_task_func():
    password = "password123"
    PREFIX = "ME"
    SALT_LENGTH = 16
    expected_result = "MEpassword123"

    result = task_func(password, PREFIX, SALT_LENGTH)

    assert result == expected_result

def test_task_func_invalid_salt_length():
    password = "password123"
    PREFIX = "ME"
    SALT_LENGTH = -1

    with pytest.raises(ValueError):
        task_func(password, PREFIX, SALT_LENGTH)