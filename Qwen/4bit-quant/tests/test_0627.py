import pytest
from src_0627 import task_func
import pytz
from dateutil.parser import parse

def test_task_func_valid_input():
    date_str = "2023-10-05 14:30:00"
    from_tz = "America/New_York"
    result, to_tz = task_func(date_str, from_tz)
    
    assert isinstance(result, str)
    assert isinstance(to_tz, str)
    assert to_tz in pytz.all_timezones

def test_task_func_invalid_timezone():
    date_str = "2023-10-05 14:30:00"
    from_tz = "Invalid/Timezone"
    
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(date_str, from_tz)

def test_task_func_invalid_date_format():
    date_str = "2023-10-05T14:30:00"  # Incorrect format
    from_tz = "America/New_York"
    
    with pytest.raises(ValueError):
        task_func(date_str, from_tz)

def test_task_func_edge_case_date():
    date_str = "1970-01-01 00:00:00"
    from_tz = "UTC"
    result, to_tz = task_func(date_str, from_tz)
    
    assert isinstance(result, str)
    assert isinstance(to_tz, str)
    assert to_tz in pytz.all_timezones