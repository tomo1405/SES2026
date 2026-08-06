import pytest
from src_0649 import task_func
from dateutil.parser import parse
from datetime import timedelta

def test_task_func():
    date_str = "2023-01-01"
    given_date = parse(date_str)
    next_day = given_date

    while True:
        next_day = next_day + timedelta(days=1)

        # Monday to Friday are business days
        if 0 <= next_day.weekday() < 5:
            break

    expected_result = next_day
    actual_result = task_func(date_str)
    assert actual_result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_ weekend_input():
    date_str = "2023-01-03"
    given_date = parse(date_str)
    next_day = given_date

    while True:
        next_day = next_day + timedelta(days=1)

        # Monday to Friday are business days
        if 0 <= next_day.weekday() < 5:
            break

    expected_result = next_day
    actual_result = task_func(date_str)
    assert actual_result == expected_result, "Task function returned an incorrect result"