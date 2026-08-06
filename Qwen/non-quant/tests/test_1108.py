import pytest
from src_1108 import task_func
import pytz
from datetime import datetime

def test_task_func_valid_unix_timestamp():
    # Test with a valid Unix timestamp and a valid timezone
    unix_timestamp = 1633072800  # October 1, 2021, 00:00:00 UTC
    target_timezone = 'America/New_York'
    expected_output = '2021-10-01 19:00:00'  # Adjusted for Eastern Daylight Time (EDT)
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_invalid_timezone():
    # Test with an invalid timezone
    unix_timestamp = 1633072800
    target_timezone = 'Invalid/Timezone'
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(unix_timestamp, target_timezone)

def test_task_func_negative_unix_timestamp():
    # Test with a negative Unix timestamp (before Unix epoch)
    unix_timestamp = -1
    target_timezone = 'UTC'
    expected_output = '1969-12-31 23:59:59'
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_zero_unix_timestamp():
    # Test with a zero Unix timestamp (Unix epoch)
    unix_timestamp = 0
    target_timezone = 'UTC'
    expected_output = '1970-01-01 00:00:00'
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_max_unix_timestamp():
    # Test with the maximum Unix timestamp value (2038-01-19 03:14:07 UTC)
    unix_timestamp = 2147483647
    target_timezone = 'UTC'
    expected_output = '2038-01-19 03:14:07'
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_different_timezone():
    # Test with a different timezone (e.g., Japan Standard Time)
    unix_timestamp = 1633072800
    target_timezone = 'Asia/Tokyo'
    expected_output = '2021-10-02 02:00:00'  # Adjusted for Japan Standard Time (JST)
    assert task_func(unix_timestamp, target_timezone) == expected_output