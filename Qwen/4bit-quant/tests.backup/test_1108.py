import pytest
from src_1108 import task_func

def test_task_func_valid_input():
    # Test with a known Unix timestamp and timezone
    unix_timestamp = 1633072800  # October 1, 2021, 00:00:00 UTC
    target_timezone = 'America/New_York'
    expected_output = '2021-10-01 19:00:00'  # Expected output in New York timezone
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_invalid_timezone():
    # Test with an invalid timezone
    unix_timestamp = 1633072800
    target_timezone = 'Invalid/Timezone'
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(unix_timestamp, target_timezone)

def test_task_func_negative_timestamp():
    # Test with a negative Unix timestamp
    unix_timestamp = -1
    target_timezone = 'UTC'
    with pytest.raises(OSError):  # Raises OSError on invalid timestamp
        task_func(unix_timestamp, target_timezone)

def test_task_func_zero_timestamp():
    # Test with a zero Unix timestamp (Unix epoch)
    unix_timestamp = 0
    target_timezone = 'Europe/London'
    expected_output = '1970-01-01 00:00:00'
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_max_timestamp():
    # Test with the maximum possible Unix timestamp
    unix_timestamp = 2147483647  # Maximum 32-bit signed integer
    target_timezone = 'Asia/Tokyo'
    expected_output = '2038-01-19 03:14:07'
    assert task_func(unix_timestamp, target_timezone) == expected_output