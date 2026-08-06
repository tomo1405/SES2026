import pytest
import pytz
from src_0302 import task_func


def test_task_func():
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = 0.8775825618903728
    result = task_func(date_str, from_tz, to_tz)
    assert result == expected_result

def test_task_func_with_different_input():
    date_str = "2020-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = 0.9999999999999999
    result = task_func(date_str, from_tz, to_tz)
    assert result == expected_result

def test_task_func_with_invalid_input():
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "Invalid_Time_Zone"
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(date_str, from_tz, to_tz)