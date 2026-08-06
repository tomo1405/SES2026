import pytest
from src_1108 import task_func

def test_task_func():
    # Test case 1: Convert a Unix timestamp to a datetime object in the UTC timezone
    unix_timestamp = 1647225600
    target_timezone = 'UTC'
    expected_datetime = '2022-03-12 00:00:00'
    assert task_func(unix_timestamp, target_timezone) == expected_datetime

    # Test case 2: Convert a Unix timestamp to a datetime object in a non-UTC timezone
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone) == expected_datetime

    # Test case 3: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime

    # Test case 4: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime

    # Test case 5: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime

    # Test case 6: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime

    # Test case 7: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime

    # Test case 8: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime

    # Test case 9: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime

    # Test case 10: Convert a Unix timestamp to a datetime object in a non-UTC timezone with a different format
    unix_timestamp = 1647225600
    target_timezone = 'America/New_York'
    expected_datetime = '2022-03-11 19:00:00'
    assert task_func(unix_timestamp, target_timezone, '%Y-%m-%d %H:%M:%S %Z') == expected_datetime