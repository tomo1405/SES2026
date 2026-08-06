from datetime import datetime

import pytest
from src_0257 import task_func


def test_task_func_valid_input():
    utc_datetime = datetime.utcnow()
    salt = 'salt'
    password_length = 10
    seed = 0
    expected_password_json_str = '{"hashed_password": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"}'

    password_json_str = task_func(utc_datetime, salt, password_length, seed)

    assert password_json_str == expected_password_json_str

def test_task_func_invalid_input():
    utc_datetime = "2022-01-01 00:00:00"
    salt = 1234
    password_length = "10"
    seed = "0"

    with pytest.raises(ValueError):
        task_func(utc_datetime, salt, password_length, seed)