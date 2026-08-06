import pytest
from src_0649 import task_func

def test_task_func():
    # Test case 1: Given date is a business day
    given_date = "2022-01-03"
    expected_date = "2022-01-04"
    assert task_func(given_date) == expected_date

    # Test case 2: Given date is a weekend
    given_date = "2022-01-02"
    expected_date = "2022-01-03"
    assert task_func(given_date) == expected_date

    # Test case 3: Given date is a holiday
    given_date = "2022-01-01"
    expected_date = "2022-01-03"
    assert task_func(given_date) == expected_date

    # Test case 4: Given date is a leap day
    given_date = "2020-02-29"
    expected_date = "2020-03-01"
    assert task_func(given_date) == expected_date

    # Test case 5: Given date is a leap year
    given_date = "2020-02-28"
    expected_date = "2020-03-01"
    assert task_func(given_date) == expected_date