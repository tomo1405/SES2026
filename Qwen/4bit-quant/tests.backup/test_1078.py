import pytest
from src_1078 import task_func

def test_task_func_with_valid_input():
    time_strings = ["01/01/23 12:00:00.000", "01/01/23 13:00:00.000"]
    timezone = "America/New_York"
    assert task_func(time_strings, timezone) == 3600.0

def test_task_func_with_single_time_string():
    time_strings = ["01/01/23 12:00:00.000"]
    timezone = "America/New_York"
    assert task_func(time_strings, timezone) == 0.0

def test_task_func_with_empty_time_strings():
    time_strings = []
    timezone = "America/New_York"
    assert task_func(time_strings, timezone) == 0.0

def test_task_func_with_different_timezones():
    time_strings = ["01/01/23 12:00:00.000", "01/01/23 15:00:00.000"]
    timezone = "Europe/London"
    assert task_func(time_strings, timezone) == 10800.0

def test_task_func_with_fractional_seconds():
    time_strings = ["01/01/23 12:00:00.123", "01/01/23 12:00:01.456"]
    timezone = "UTC"
    assert task_func(time_strings, timezone) == 1.333

def test_task_func_with_invalid_time_format():
    time_strings = ["01-01-23 12:00:00.000", "01/01/23 13:00:00.000"]
    timezone = "America/New_York"
    with pytest.raises(ValueError):
        task_func(time_strings, timezone)

def test_task_func_with_invalid_timezone():
    time_strings = ["01/01/23 12:00:00.000", "01/01/23 13:00:00.000"]
    timezone = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(time_strings, timezone)