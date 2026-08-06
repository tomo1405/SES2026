import pytest
from src_0649 import task_func
from dateutil.parser import parse
from datetime import timedelta

def test_task_func():
    # Test case 1: Given date is a business day
    given_date = parse("2022-01-01")
    expected_result = parse("2022-01-04")
    assert task_func(given_date) == expected_result

    # Test case 2: Given date is a weekend
    given_date = parse("2022-01-02")
    expected_result = parse("2022-01-03")
    assert task_func(given_date) == expected_result

    # Test case 3: Given date is a holiday
    given_date = parse("2022-01-03")
    expected_result = parse("2022-01-04")
    assert task_func(given_date) == expected_result

    # Test case 4: Given date is a leap year
    given_date = parse("2020-02-29")
    expected_result = parse("2020-03-02")
    assert task_func(given_date) == expected_result

    # Test case 5: Given date is a non-leap year
    given_date = parse("2021-02-28")
    expected_result = parse("2021-03-01")
    assert task_func(given_date) == expected_result