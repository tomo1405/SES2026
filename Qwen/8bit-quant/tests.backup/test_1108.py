import pytest
from src_1108 import task_func

def test_task_func_valid_timestamp_and_timezone():
    # Test with a valid Unix timestamp and timezone
    unix_timestamp = 1633072800  # 2021-10-01 00:00:00 UTC
    target_timezone = 'America/New_York'
    expected_output = '2021-09-30 20:00:00'  # Expected output in Eastern Time
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_invalid_timezone():
    # Test with an invalid timezone
    unix_timestamp = 1633072800
    target_timezone = 'Invalid/Timezone'
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(unix_timestamp, target_timezone)

def test_task_func_negative_timestamp():
    # Test with a negative Unix timestamp (before Unix epoch)
    unix_timestamp = -1
    target_timezone = 'UTC'
    expected_output = '1969-12-31 23:59:59'
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_zero_timestamp():
    # Test with a zero Unix timestamp (Unix epoch)
    unix_timestamp = 0
    target_timezone = 'UTC'
    expected_output = '1970-01-01 00:00:00'
    assert task_func(unix_timestamp, target_timezone) == expected_output

def test_task_func_non_string_timezone():
    # Test with a non-string timezone
    unix_timestamp = 1633072800
    target_timezone = 12345
    with pytest.raises(AttributeError):
        task_func(unix_timestamp, target_timezone)