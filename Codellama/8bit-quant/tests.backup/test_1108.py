import pytest
from src_1108 import task_func

def test_task_func():
    # Test case 1: Convert a Unix timestamp to a datetime object in the target timezone
    unix_timestamp = 1643230400
    target_timezone = 'America/New_York'
    expected_datetime = '2022-01-20 00:00:00'
    assert task_func(unix_timestamp, target_timezone) == expected_datetime

    # Test case 2: Convert a Unix timestamp to a datetime object in a different target timezone
    unix_timestamp = 1643230400
    target_timezone = 'Asia/Tokyo'
    expected_datetime = '2022-01-20 09:00:00'
    assert task_func(unix_timestamp, target_timezone) == expected_datetime

    # Test case 3: Convert a Unix timestamp to a datetime object in the target timezone with a different format
    unix_timestamp = 1643230400
    target_timezone = 'America/New_York'
    expected_datetime = '2022-01-20 00:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S') == expected_datetime

    # Test case 4: Convert a Unix timestamp to a datetime object in the target timezone with a different format and a different timezone
    unix_timestamp = 1643230400
    target_timezone = 'Asia/Tokyo'
    expected_datetime = '2022-01-20 09:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S') == expected_datetime