import pytest
from src_0627 import task_func
from random import choice
import pytz
from dateutil.parser import parse
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

def test_task_func():
    date_str = '2023-01-01 12:00:00'
    from_tz = 'America/New_York'
    expected_converted_date = '2023-01-01 20:00:00'
    expected_to_tz = 'Asia/Tokyo'

    converted_date, to_tz = task_func(date_str, from_tz)

    assert converted_date == expected_converted_date
    assert to_tz == expected_to_tz

def test_task_func_with_invalid_date_str():
    date_str = 'invalid_date'
    from_tz = 'America/New_York'

    with pytest.raises(ValueError):
        task_func(date_str, from_tz)

def test_task_func_with_invalid_from_tz():
    date_str = '2023-01-01 12:00:00'
    from_tz = 'Invalid/Timezones'

    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(date_str, from_tz)