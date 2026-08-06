import pytest
import pytz
from src_1075 import task_func


def test_task_func():
    time_string = "01/01/22 00:00:00.000000"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_output = "01/01/22 05:00:00.000000"

    output = task_func(time_string, from_tz, to_tz)

    assert output == expected_output

def test_task_func_invalid_time_string():
    time_string = "01/01/22 24:00:00.000000"
    from_tz = "UTC"
    to_tz = "US/Eastern"

    with pytest.raises(ValueError):
        task_func(time_string, from_tz, to_tz)

def test_task_func_invalid_from_tz():
    time_string = "01/01/22 00:00:00.000000"
    from_tz = "Invalid_Time_Zone"
    to_tz = "US/Eastern"

    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(time_string, from_tz, to_tz)

def test_task_func_invalid_to_tz():
    time_string = "01/01/22 00:00:00.000000"
    from_tz = "UTC"
    to_tz = "Invalid_Time_Zone"

    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(time_string, from_tz, to_tz)