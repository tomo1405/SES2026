import pytest
from src_0548 import task_func

def test_task_func():
    # Test with a valid password and salt length
    password = "password123"
    salt_length = 8
    expected_result = "gAAAAABbhj5JXZXJYXK1w100000"
    assert task_func(password, salt_length) == expected_result

    # Test with a valid password and salt length of 0
    password = "password123"
    salt_length = 0
    expected_result = "gAAAAABbhj5JXZXJYXK1w100000"
    assert task_func(password, salt_length) == expected_result

    # Test with a valid password and salt length of 10
    password = "password123"
    salt_length = 10
    expected_result = "gAAAAABbhj5JXZXJYXK1w100000"
    assert task_func(password, salt_length) == expected_result

    # Test with a valid password and salt length of 100
    password = "password123"
    salt_length = 100
    expected_result = "gAAAAABbhj5JXZXJYXK1w100000"
    assert task_func(password, salt_length) == expected_result

    # Test with an invalid password
    password = ""
    salt_length = 8
    expected_result = "Invalid password"
    assert task_func(password, salt_length) == expected_result

    # Test with an invalid salt length
    password = "password123"
    salt_length = -1
    expected_result = "Invalid salt length"
    assert task_func(password, salt_length) == expected_result