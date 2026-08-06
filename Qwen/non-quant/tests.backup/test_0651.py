import pytest
from src_0651 import task_func
from datetime import datetime
import pytz
from dateutil.parser import parse

def test_task_func():
    # Test with a date in UTC
    date_str = "2023-12-31T23:59:59Z"
    tz_str = "UTC"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day

    # Test with a date in EST
    date_str = "2023-12-31T18:59:59-05:00"
    tz_str = "America/New_York"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day

    # Test with a date in PST
    date_str = "2023-12-31T15:59:59-08:00"
    tz_str = "America/Los_Angeles"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day

    # Test with a date in JST
    date_str = "2023-12-31T15:59:59+09:00"
    tz_str = "Asia/Tokyo"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day

    # Test with a date in a different year
    date_str = "2022-12-31T23:59:59Z"
    tz_str = "UTC"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day

    # Test with a date on New Year's Day
    date_str = "2023-01-01T00:00:00Z"
    tz_str = "UTC"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day

    # Test with a date just before New Year's Day
    date_str = "2022-12-31T23:59:59Z"
    tz_str = "UTC"
    result = task_func(date_str, tz_str)
    assert result == 86400  # 1 day until New Year's Day

    # Test with a date just after New Year's Day
    date_str = "2023-01-01T00:00:01Z"
    tz_str = "UTC"
    result = task_func(date_str, tz_str)
    assert result > 86400  # More than 1 day until New Year's Day

    # Test with a date in a non-existent timezone
    date_str = "2023-12-31T23:59:59Z"
    tz_str = "NonExistent/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, tz_str)

    # Test with a date in an invalid format
    date_str = "2023-13-32T23:59:59Z"
    tz_str = "UTC"
    with pytest.raises(ValueError):
        task_func(date_str, tz_str)