import pytest
from src_1046 import task_func

def test_task_func():
    # Test case 1: given date is in the past
    given_date = "2020-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 2: given date is in the future
    given_date = "2022-01-01"
    expected_result = 2000000
    assert task_func(given_date) == expected_result

    # Test case 3: given date is in the past, but leap seconds have occurred
    given_date = "2010-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 4: given date is in the future, but leap seconds have occurred
    given_date = "2025-01-01"
    expected_result = 2000000
    assert task_func(given_date) == expected_result

    # Test case 5: given date is in the past, but leap seconds have not occurred
    given_date = "2010-01-01"
    expected_result = 1000000
    assert task_func(given_date) == expected_result

    # Test case 6: given date is in the future, but leap seconds have not occurred
    given_date = "2025-01-01"
    expected_result = 2000000
    assert task_func(given_date) == expected_result