from datetime import datetime

import pytest
from src_0257 import task_func


def test_task_func_valid_input():
    utc_datetime = datetime.utcnow()
    salt = 'salt'
    password_length = 10
    seed = 0
    expected_password_json_str = '{"hashed_password": "hashed_password_value"}'

    password_json_str = task_func(utc_datetime, salt, password_length, seed)

    assert password_json_str == expected_password_json_str

def test_task_func_invalid_input():
    utc_datetime = "invalid_datetime"
    salt = 1234
    password_length = "invalid_length"
    seed = "invalid_seed"

    with pytest.raises(ValueError):
        task_func(utc_datetime, salt, password_length, seed)