python
import pytest
from src_0649 import task_func

def test_task_func():
    # Test case 1
    date_str = "2022-01-01"
    expected_date = "2022-01-02"
    assert task_func(date_str).strftime("%Y-%m-%d") == expected_date

    # Test case 2
    date_str = "2022-01-05"
    expected_date = "2022-01-08"
    assert task_func(date_str).strftime("%Y-%m-%d") == expected_date

    # Test case 3
    date_str = "2022-01-15"
    expected_date = "2022-01-22"
    assert task_func(date_str).strftime("%Y-%m-%d") == expected_date

    # Test case 4
    date_str = "2022-02-28"
    expected_date = "2022-03-01"
    assert task_func(date_str).strftime("%Y-%m-%d") == expected_date

    # Test case 5
    date_str = "2022-04-30"
    expected_date = "2022-05-01"
    assert task_func(date_str).strftime("%Y-%m-%d") == expected_date

    # Test case 6
    date_str = "2022-12-31"
    expected_date = "2023-01-01"
    assert task_func(date_str).strftime("%Y-%m-%d") == expected_date