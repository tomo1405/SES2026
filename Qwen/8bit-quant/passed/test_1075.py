import pytest
from src_1075 import task_func
from dateutil.parser import parse
import pytz

def test_task_func_same_timezone():
    time_string = "01/01/23 12:00:00.000000"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    expected_output = "01/01/23 12:00:00.000000"
    assert task_func(time_string, from_tz, to_tz) == expected_output

def test_task_func_different_timezones():
    time_string = "01/01/23 12:00:00.000000"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    expected_output = "01/01/23 17:00:00.000000"
    assert task_func(time_string, from_tz, to_tz) == expected_output

def test_task_func_daylight_saving():
    time_string = "01/03/23 01:30:00.000000"  # DST transition in New York
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    expected_output = "01/03/23 06:30:00.000000"
    assert task_func(time_string, from_tz, to_tz) == expected_output

def test_task_func_invalid_time_string():
    time_string = "invalid_time"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    with pytest.raises(ValueError):
        task_func(time_string, from_tz, to_tz)

def test_task_func_invalid_timezone():
    time_string = "01/01/23 12:00:00.000000"
    from_tz = "Invalid/Timezone"
    to_tz = "Europe/London"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(time_string, from_tz, to_tz)