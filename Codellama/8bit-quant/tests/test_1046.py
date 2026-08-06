import pytest
from src_1046 import task_func

def test_task_func():
    # Test case 1: Given date is in the past
    given_date = "2022-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 2: Given date is in the future
    given_date = "2022-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 3: Given date is in the present
    given_date = "2022-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 4: Given date is in the past, but not a leap year
    given_date = "2021-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 5: Given date is in the future, but not a leap year
    given_date = "2023-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 6: Given date is in the present, but not a leap year
    given_date = "2022-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result