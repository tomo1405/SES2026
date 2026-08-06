import pytest
from src_0649 import task_func
from dateutil.parser import parse

def test_task_func_next_business_day():
    # Test with a date that is a Saturday
    input_date = "2023-10-07"
    expected_output = parse("2023-10-09")
    assert task_func(input_date) == expected_output

    # Test with a date that is a Sunday
    input_date = "2023-10-08"
    expected_output = parse("2023-10-09")
    assert task_func(input_date) == expected_output

    # Test with a date that is a Friday
    input_date = "2023-10-06"
    expected_output = parse("2023-10-09")
    assert task_func(input_date) == expected_output

    # Test with a date that is a Wednesday
    input_date = "2023-10-04"
    expected_output = parse("2023-10-05")
    assert task_func(input_date) == expected_output

    # Test with a date that is a Monday
    input_date = "2023-10-02"
    expected_output = parse("2023-10-03")
    assert task_func(input_date) == expected_output

def test_task_func_invalid_date():
    with pytest.raises(ValueError):
        task_func("invalid-date")

def test_task_func_leap_year():
    # Test with a leap year date
    input_date = "2024-02-29"
    expected_output = parse("2024-03-01")
    assert task_func(input_date) == expected_output

def test_task_func_non_leap_year():
    # Test with a non-leap year date
    input_date = "2023-02-28"
    expected_output = parse("2023-03-01")
    assert task_func(input_date) == expected_output