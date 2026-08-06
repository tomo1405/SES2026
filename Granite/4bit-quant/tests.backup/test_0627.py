import pytest
from src_0627 import task_func

def test_task_func():
    date_str = '2023-01-01 12:00:00'
    from_tz = 'America/New_York'
    expected_output = ('2023-01-01 07:00:00', 'America/New_York')
    output = task_func(date_str, from_tz)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_date_str():
    date_str = 'invalid_date'
    from_tz = 'America/New_York'
    with pytest.raises(ValueError):
        task_func(date_str, from_tz)

def test_task_func_with_invalid_from_tz():
    date_str = '2023-01-01 12:00:00'
    from_tz = 'invalid_timezone'
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(date_str, from_tz)