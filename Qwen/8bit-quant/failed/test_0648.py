import pytest
from src_0648 import task_func
from datetime import datetime
import pytz

def test_task_func_same_timezones():
    date_str = "2023-10-01T12:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert result == 0

def test_task_func_utc_to_est():
    date_str = "2023-10-01T12:00:00"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    result = task_func(date_str, from_tz, to_tz)
    expected = (datetime.now(pytz.utc) - datetime(2023, 10, 1, 12, 0, 0, tzinfo=pytz.utc)).total_seconds()
    assert abs(result - expected) < 3600  # Allow for a 1-hour margin of error due to daylight saving changes

def test_task_func_est_to_utc():
    date_str = "2023-10-01T07:00:00"
    from_tz = "US/Eastern"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    expected = (datetime.now(pytz.utc) - datetime(2023, 10, 1, 12, 0, 0, tzinfo=pytz.utc)).total_seconds()
    assert abs(result - expected) < 3600  # Allow for a 1-hour margin of error due to daylight saving changes

def test_task_func_invalid_timezone():
    date_str = "2023-10-01T12:00:00"
    from_tz = "UTC"
    to_tz = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz, to_tz)

def test_task_func_invalid_date_format():
    date_str = "2023-10-01 12:00:00"  # Incorrect format
    from_tz = "UTC"
    to_tz = "US/Eastern"
    with pytest.raises(ValueError):
        task_func(date_str, from_tz, to_tz)