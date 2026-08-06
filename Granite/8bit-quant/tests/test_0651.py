import pytest
from src_0651 import task_func
from datetime import datetime
import pytz
from dateutil.parser import parse

def test_task_func():
    date_str = "2022-12-31 23:59:59"
    tz_str = "UTC"
    expected_result = 31536000

    result = task_func(date_str, tz_str)

    assert result == expected_result

def test_task_func_with_timezone():
    date_str = "2022-12-31 23:59:59"
    tz_str = "America/New_York"
    expected_result = 31539600

    result = task_func(date_str, tz_str)

    assert result == expected_result

def test_task_func_with_invalid_date_str():
    date_str = "2022-13-31 23:59:59"
    tz_str = "UTC"

    with pytest.raises(ValueError):
        task_func(date_str, tz_str)

def test_task_func_with_invalid_tz_str():
    date_str = "2022-12-31 23:59:59"
    tz_str = "Invalid_timezone"

    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(date_str, tz_str)