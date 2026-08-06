import pytest
from src_0648 import task_func
from datetime import datetime
import pytz
from dateutil.parser import parse

def test_task_func_same_timezones():
    date_str = "2023-10-01T12:00:00"
    from_tz = "UTC"
    to_tz = "UTC"
    result = task_func(date_str, from_tz, to_tz)
    assert result == 0

def test_task_func_different_timezones():
    date_str = "2023-10-01T12:00:00"
    from_tz = "UTC"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    # Assuming New York is 4 hours behind UTC during this period
    assert result == 14400

def test_task_func_dst_change():
    date_str = "2023-03-12T02:00:00"  # Spring DST change in the US
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    result = task_func(date_str, from_tz, to_tz)
    assert result == 0

def test_task_func_invalid_date_str():
    date_str = "invalid-date"
    from_tz = "UTC"
    to_tz = "UTC"
    with pytest.raises(ValueError):
        task_func(date_str, from_tz, to_tz)

def test_task_func_invalid_timezone():
    date_str = "2023-10-01T12:00:00"
    from_tz = "Invalid/Timezone"
    to_tz = "UTC"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz, to_tz)