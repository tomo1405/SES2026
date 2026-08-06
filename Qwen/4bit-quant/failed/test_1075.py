import pytest
from src_1075 import task_func

def test_task_func_same_timezone():
    time_string = "25/12/23 14:30:00.000"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    expected_output = "25/12/23 14:30:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_output

def test_task_func_different_timezones():
    time_string = "25/12/23 14:30:00.000"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    expected_output = "25/12/23 20:30:00.000"  # New York is 6 hours behind London
    assert task_func(time_string, from_tz, to_tz) == expected_output

def test_task_func_dayfirst_parsing():
    time_string = "12/25/23 14:30:00.000"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    expected_output = "25/12/23 20:30:00.000"  # Day first should be respected
    assert task_func(time_string, from_tz, to_tz) == expected_output

def test_task_func_invalid_timezone():
    time_string = "25/12/23 14:30:00.000"
    from_tz = "Invalid/Timezone"
    to_tz = "Europe/London"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(time_string, from_tz, to_tz)

def test_task_func_invalid_time_string():
    time_string = "25-12-23 14:30:00.000"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    with pytest.raises(ValueError):
        task_func(time_string, from_tz, to_tz)