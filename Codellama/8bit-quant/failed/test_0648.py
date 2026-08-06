import pytest
from src_0648 import task_func

def test_task_func():
    # Test case 1: Given date is in the past
    date_str = "2022-01-01 12:00:00"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = -86400
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 2: Given date is in the future
    date_str = "2022-01-01 12:00:00"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = 86400
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 3: Given date is in the same timezone as the destination timezone
    date_str = "2022-01-01 12:00:00"
    from_tz = "US/Eastern"
    to_tz = "US/Eastern"
    expected_result = 0
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 4: Given date is in a different timezone than the destination timezone
    date_str = "2022-01-01 12:00:00"
    from_tz = "US/Eastern"
    to_tz = "US/Pacific"
    expected_result = -3600
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 5: Given date is in a different timezone than the destination timezone
    date_str = "2022-01-01 12:00:00"
    from_tz = "US/Eastern"
    to_tz = "US/Pacific"
    expected_result = 3600
    assert task_func(date_str, from_tz, to_tz) == expected_result