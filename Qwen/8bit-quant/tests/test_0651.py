import pytest
from src_0651 import task_func
from datetime import datetime
import pytz
from dateutil.parser import parse

def test_task_func_same_timezone():
    date_str = "2023-12-31T23:59:59"
    tz_str = "UTC"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day in UTC

def test_task_func_different_timezone():
    date_str = "2023-12-31T23:59:59"
    tz_str = "America/New_York"
    result = task_func(date_str, tz_str)
    assert result == 7200  # 2 hours until New Year's Day in EST

def test_task_func_dst_change():
    date_str = "2023-11-05T01:59:59"  # Just before DST change in US/Eastern
    tz_str = "US/Eastern"
    result = task_func(date_str, tz_str)
    assert result == 31536000  # 1 year until New Year's Day

def test_task_func_leap_year():
    date_str = "2020-02-28T23:59:59"  # Leap year case
    tz_str = "UTC"
    result = task_func(date_str, tz_str)
    assert result == 86400 * 366  # 366 days until New Year's Day

def test_task_func_nonexistent_time():
    date_str = "2023-03-13T02:30:00"  # Nonexistent time due to DST in US/Eastern
    tz_str = "US/Eastern"
    with pytest.raises(ValueError):
        task_func(date_str, tz_str)

def test_task_func_invalid_timezone():
    date_str = "2023-12-31T23:59:59"
    tz_str = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, tz_str)

def test_task_func_invalid_date():
    date_str = "2023-02-30T23:59:59"  # Invalid date
    tz_str = "UTC"
    with pytest.raises(ValueError):
        task_func(date_str, tz_str)