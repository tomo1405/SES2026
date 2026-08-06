from datetime import datetime

import pytest
from src_0257 import task_func


def test_task_func():
    # Test if the function raises an error when the input is not a datetime object
    with pytest.raises(ValueError):
        task_func(12345, 'salt')

    # Test if the function raises an error when the salt is not a string
    with pytest.raises(ValueError):
        task_func(datetime.now(), 12345)

    # Test if the function returns a valid JSON string
    password_json_str = task_func(datetime.now(), 'salt')
    assert isinstance(password_json_str, str)
    assert password_json_str.startswith('"') and password_json_str.endswith('"')

    # Test if the function returns a valid password
    password = task_func(datetime.now(), 'salt', 10)
    assert isinstance(password, str)
    assert len(password) == 10

    # Test if the function returns a valid hashed password
    hashed_password = task_func(datetime.now(), 'salt', 10, 0)
    assert isinstance(hashed_password, str)
    assert len(hashed_password) == 64