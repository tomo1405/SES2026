import pytest
from src_0649 import task_func
from dateutil.parser import parse
from datetime import datetime, timedelta

def test_task_func_next_business_day():
    # Test with a Saturday
    input_date = "2023-10-07"
    expected_output = parse("2023-10-09")
    assert task_func(input_date) == expected_output

    # Test with a Sunday
    input_date = "2023-10-08"
    expected_output = parse("2023-10-09")
    assert task_func(input_date) == expected_output

    # Test with a Wednesday
    input_date = "2023-10-11"
    expected_output = parse("2023-10-12")
    assert task_func(input_date) == expected_output

    # Test with a Friday
    input_date = "2023-10-13"
    expected_output = parse("2023-10-16")
    assert task_func(input_date) == expected_output

def test_task_func_same_day():
    # Test with a Monday
    input_date = "2023-10-09"
    expected_output = parse("2023-10-10")
    assert task_func(input_date) == expected_output

    # Test with a Tuesday
    input_date = "2023-10-10"
    expected_output = parse("2023-10-11")
    assert task_func(input_date) == expected_output

def test_task_func_invalid_date():
    # Test with an invalid date string
    input_date = "invalid-date"
    with pytest.raises(ValueError):
        task_func(input_date)