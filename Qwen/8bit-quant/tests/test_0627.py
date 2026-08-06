import pytest
import pytz
from dateutil.parser import parse
from src_0627 import task_func


def test_task_func_valid_input():
    date_str = "2023-10-01 12:00:00"
    from_tz = "UTC"
    result = task_func(date_str, from_tz)
    converted_date, to_tz = result
    
    # Parse the original date and convert it to the randomly chosen timezone
    original_date = parse(date_str).replace(tzinfo=pytz.utc)
    to_tz_obj = pytz.timezone(to_tz)
    expected_converted_date = original_date.astimezone(to_tz_obj).strftime('%Y-%m-%d %H:%M:%S')
    
    assert converted_date == expected_converted_date
    assert to_tz in TIMEZONES

def test_task_func_invalid_date_format():
    date_str = "2023-10-01 12:00"  # Missing seconds
    from_tz = "UTC"
    with pytest.raises(ValueError):
        task_func(date_str, from_tz)

def test_task_func_invalid_timezone():
    date_str = "2023-10-01 12:00:00"
    from_tz = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz)

def test_task_func_empty_date_string():
    date_str = ""
    from_tz = "UTC"
    with pytest.raises(ValueError):
        task_func(date_str, from_tz)

def test_task_func_empty_timezone():
    date_str = "2023-10-01 12:00:00"
    from_tz = ""
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz)