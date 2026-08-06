import pytest
import pytz
from src_0562 import task_func


def test_task_func_valid_conversion():
    date_str = "2023-10-01 12:00:00"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    expected_output = "2023-10-01 17:00:00"  # New York is 5 hours behind London
    assert task_func(date_str, from_tz, to_tz) == expected_output

def test_task_func_same_timezone():
    date_str = "2023-10-01 12:00:00"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    expected_output = "2023-10-01 12:00:00"
    assert task_func(date_str, from_tz, to_tz) == expected_output

def test_task_func_invalid_date_str():
    date_str = "invalid-date"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    with pytest.raises(ValueError):
        task_func(date_str, from_tz, to_tz)

def test_task_func_invalid_timezone():
    date_str = "2023-10-01 12:00:00"
    from_tz = "Invalid/Timezone"
    to_tz = "Europe/London"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz, to_tz)

def test_task_func_dst_change():
    date_str = "2023-03-12 01:59:00"  # Just before DST change in New York
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    expected_output = "2023-03-12 07:59:00"
    assert task_func(date_str, from_tz, to_tz) == expected_output