import pytest
from src_1046 import task_func

def test_task_func():
    # Test case 1: Given date is in the past
    given_date = "2020-01-01"
    expected_result = 1577836800
    assert task_func(given_date) == expected_result

    # Test case 2: Given date is in the future
    given_date = "2022-01-01"
    expected_result = 1640995200
    assert task_func(given_date) == expected_result

    # Test case 3: Given date is in the present
    given_date = "2021-01-01"
    expected_result = 1609459200
    assert task_func(given_date) == expected_result

    # Test case 4: Given date is a leap year
    given_date = "2020-02-29"
    expected_result = 1583020800
    assert task_func(given_date) == expected_result

    # Test case 5: Given date is not a leap year
    given_date = "2021-02-28"
    expected_result = 1612864000
    assert task_func(given_date) == expected_result