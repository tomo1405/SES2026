import pytest
from src_0649 import task_func
from dateutil.parser import parse
from datetime import timedelta

def test_task_func():
    # Test case 1: Next business day for a Thursday
    given_date_str = "2023-01-15"
    expected_next_day = parse("2023-01-17")
    actual_next_day = task_func(given_date_str)
    assert actual_next_day == expected_next_day

    # Test case 2: Next business day for a Saturday
    given_date_str = "2023-01-17"
    expected_next_day = parse("2023-01-20")
    actual_next_day = task_func(given_date_str)
    assert actual_next_day == expected_next_day

    # Test case 3: Next business day for a Sunday
    given_date_str = "2023-01-18"
    expected_next_day = parse("2023-01-20")
    actual_next_day = task_func(given_date_str)
    assert actual_next_day == expected_next_day

    # Test case 4: Next business day for a Monday
    given_date_str = "2023-01-19"
    expected_next_day = parse("2023-01-20")
    actual_next_day = task_func(given_date_str)
    assert actual_next_day == expected_next_day

    # Test case 5: Next business day for a Tuesday
    given_date_str = "2023-01-20"
    expected_next_day = parse("2023-01-21")
    actual_next_day = task_func(given_date_str)
    assert actual_next_day == expected_next_day

    # Test case 6: Next business day for a Wednesday
    given_date_str = "2023-01-21"
    expected_next_day = parse("2023-01-24")
    actual_next_day = task_func(given_date_str)
    assert actual_next_day == expected_next_day