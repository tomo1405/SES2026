import pytest
from src_0651 import task_func
from datetime import datetime
import pytz

def test_task_func_same_year():
    date_str = "2023-12-31T23:59:59"
    tz_str = "America/New_York"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 24 hours in seconds

def test_task_func_next_year():
    date_str = "2023-01-01T00:00:00"
    tz_str = "America/New_York"
    result = task_func(date_str, tz_str)
    assert result == 31536000  # 365 days in seconds

def test_task_func_different_timezone():
    date_str = "2023-12-31T23:59:59"
    tz_str = "Europe/London"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 24 hours in seconds

def test_task_func_invalid_date():
    date_str = "invalid-date"
    tz_str = "America/New_York"
    with pytest.raises(ValueError):
        task_func(date_str, tz_str)

def test_task_func_invalid_timezone():
    date_str = "2023-12-31T23:59:59"
    tz_str = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, tz_str)