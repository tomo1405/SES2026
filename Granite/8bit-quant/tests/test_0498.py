import pytest
from src_0498 import task_func
from datetime import datetime, timedelta
import pytz
import calendar

def test_task_func_with_positive_days_in_past():
    days_in_past = 7
    expected_weekday = calendar.day_name[(datetime.now(pytz.UTC) - timedelta(days=days_in_past)).weekday()]
    actual_weekday = task_func(days_in_past)
    assert actual_weekday == expected_weekday

def test_task_func_with_zero_days_in_past():
    days_in_past = 0
    expected_weekday = calendar.day_name[(datetime.now(pytz.UTC) - timedelta(days=days_in_past)).weekday()]
    actual_weekday = task_func(days_in_past)
    assert actual_weekday == expected_weekday

def test_task_func_with_negative_days_in_past():
    days_in_past = -7
    with pytest.raises(ValueError) as excinfo:
        task_func(days_in_past)
    assert "Days in the past cannot be negative" in str(excinfo.value)