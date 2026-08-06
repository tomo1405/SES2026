import pytest
from src_0548 import task_func

def test_task_func():
    # Test with a valid password
    password = "password123"
    salt_length = 8
    expected_output = "U2FsdGVkX18zMjIzNQ=="
    assert task_func(password, salt_length) == expected_output

    # Test with a different salt length
    password = "password123"
    salt_length = 16
    expected_output = "U2FsdGVkX18zMjIzNQ=="
    assert task_func(password, salt_length) == expected_output

    # Test with a different password
    password = "password456"
    salt_length = 8
    expected_output = "U2FsdGVkX18zMjIzNQ=="
    assert task_func(password, salt_length) == expected_output

    # Test with a different salt length and password
    password = "password456"
    salt_length = 16
    expected_output = "U2FsdGVkX18zMjIzNQ=="
    assert task_func(password, salt_length) == expected_output