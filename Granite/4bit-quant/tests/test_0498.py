import pytest
from src_0498 import task_func
from datetime import datetime, timedelta
import pytz
import calendar

def test_task_func():
    # Test case 1: days_in_past is positive
    days_in_past = 7
    expected_weekday = calendar.day_name[datetime.now(pytz.UTC) - timedelta(days=days_in_past).weekday()]
    actual_weekday = task_func(days_in_past)
    assert actual_weekday == expected_weekday, "Expected weekday does not match actual weekday"

    # Test case 2: days_in_past is negative
    days_in_past = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(days_in_past)
    assert "Days in the past cannot be negative" in str(excinfo.value), "Expected error message not raised"