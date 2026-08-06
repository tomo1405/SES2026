import pytest
from src_1046 import task_func
from datetime import datetime
from dateutil.parser import parse

def test_task_func():
    given_date_str = "2022-01-01"
    given_date = parse(given_date_str)
    current_date = datetime.now()
    total_seconds = (current_date - given_date).total_seconds()
    leap_seconds = np.sum(LEAP_SECONDS >= given_date.year)
    total_seconds += leap_seconds
    expected_result = int(total_seconds)
    actual_result = task_func(given_date_str)
    assert actual_result == expected_result

def test_task_func_with_leap_seconds():
    given_date_str = "2022-06-30"
    given_date = parse(given_date_str)
    current_date = datetime.now()
    total_seconds = (current_date - given_date).total_seconds()
    leap_seconds = np.sum(LEAP_SECONDS >= given_date.year)
    total_seconds += leap_seconds
    expected_result = int(total_seconds)
    actual_result = task_func(given_date_str)
    assert actual_result == expected_result

def test_task_func_with_zero_seconds():
    given_date_str = "2022-01-01"
    given_date = parse(given_date_str)
    current_date = datetime.now()
    total_seconds = (current_date - given_date).total_seconds()
    expected_result = int(total_seconds)
    actual_result = task_func(given_date_str)
    assert actual_result == expected_result

def test_task_func_with_future_date():
    given_date_str = "2023-01-01"
    with pytest.raises(ValueError):
        task_func(given_date_str)