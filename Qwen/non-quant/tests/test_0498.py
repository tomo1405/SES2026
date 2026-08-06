import calendar
from datetime import datetime

import pytest
import pytz
from src_0498 import task_func


def test_task_func_default_days():
    # Test with default value of days_in_past (7)
    current_weekday = datetime.now(pytz.UTC).weekday()
    expected_weekday = calendar.day_name[(current_weekday - 7) % 7]
    assert task_func() == expected_weekday

def test_task_func_positive_days():
    # Test with a positive number of days in the past
    days_in_past = 3
    current_weekday = datetime.now(pytz.UTC).weekday()
    expected_weekday = calendar.day_name[(current_weekday - days_in_past) % 7]
    assert task_func(days_in_past) == expected_weekday

def test_task_func_zero_days():
    # Test with zero days in the past
    current_weekday = datetime.now(pytz.UTC).weekday()
    expected_weekday = calendar.day_name[current_weekday]
    assert task_func(0) == expected_weekday

def test_task_func_negative_days():
    # Test with a negative number of days in the past, should raise ValueError
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_large_days():
    # Test with a large number of days in the past
    days_in_past = 100
    current_weekday = datetime.now(pytz.UTC).weekday()
    expected_weekday = calendar.day_name[(current_weekday - days_in_past) % 7]
    assert task_func(days_in_past) == expected_weekday