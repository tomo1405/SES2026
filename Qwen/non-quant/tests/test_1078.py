import pytest
from src_1078 import task_func
from datetime import datetime
import pytz

def test_task_func_with_empty_list():
    assert task_func([], "UTC") == 0.0

def test_task_func_with_single_time_string():
    assert task_func(["01/01/23 12:00:00.000000"], "UTC") == 0.0

def test_task_func_with_two_time_strings_same_timezone():
    time_strings = ["01/01/23 12:00:00.000000", "01/01/23 12:01:00.000000"]
    result = task_func(time_strings, "UTC")
    assert result == 60.0

def test_task_func_with_two_time_strings_different_timezones():
    time_strings = ["01/01/23 12:00:00.000000", "01/01/23 13:00:00.000000"]
    result = task_func(time_strings, "Europe/London")
    assert result == 3600.0

def test_task_func_with_multiple_time_strings_same_timezone():
    time_strings = [
        "01/01/23 12:00:00.000000",
        "01/01/23 12:01:00.000000",
        "01/01/23 12:02:00.000000"
    ]
    result = task_func(time_strings, "UTC")
    assert result == 60.0

def test_task_func_with_multiple_time_strings_different_timezones():
    time_strings = [
        "01/01/23 12:00:00.000000",
        "01/01/23 13:00:00.000000",
        "01/01/23 14:00:00.000000"
    ]
    result = task_func(time_strings, "Europe/London")
    assert result == 3600.0

def test_task_func_with_invalid_timezone():
    time_strings = ["01/01/23 12:00:00.000000", "01/01/23 12:01:00.000000"]
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(time_strings, "Invalid/Timezone")

def test_task_func_with_invalid_time_format():
    time_strings = ["01/01/23 12:00:00", "01/01/23 12:01:00"]
    with pytest.raises(ValueError):
        task_func(time_strings, "UTC")