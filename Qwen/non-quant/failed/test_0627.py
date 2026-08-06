import pytest
from src_0627 import task_func
from dateutil.parser import parse
import pytz

def test_task_func():
    # Test with a known date and timezone
    date_str = "2023-10-01 12:00:00"
    from_tz = "America/New_York"
    expected_timezones = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

    # Parse the date string to get the original datetime object
    original_date = parse(date_str).replace(tzinfo=pytz.timezone(from_tz))

    # Call the function
    converted_date_str, to_tz = task_func(date_str, from_tz)

    # Parse the converted date string to get the datetime object
    converted_date = parse(converted_date_str).replace(tzinfo=pytz.timezone(to_tz))

    # Check if the timezone is one of the expected timezones
    assert to_tz in expected_timezones

    # Check if the conversion is correct by comparing the naive times (ignoring the timezone)
    assert original_date.replace(tzinfo=None) == converted_date.replace(tzinfo=None)

def test_task_func_invalid_timezone():
    # Test with an invalid timezone
    date_str = "2023-10-01 12:00:00"
    from_tz = "Invalid/Timezone"

    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz)

def test_task_func_invalid_date_format():
    # Test with an invalid date format
    date_str = "2023-10-01"
    from_tz = "America/New_York"

    with pytest.raises(ValueError):
        task_func(date_str, from_tz)