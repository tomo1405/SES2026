import pytest
from src_0648 import task_func

def test_task_func():
    # Test case 1: Given date is in the past
    date_str = "2022-01-01 12:00:00"
    from_tz = "UTC"
    to_tz = "America/New_York"
    expected_result = -1

    result = task_func(date_str, from_tz, to_tz)

    assert result == expected_result

    # Test case 2: Given date is in the future
    date_str = "2022-01-01 12:00:00"
    from_tz = "UTC"
    to_tz = "America/New_York"
    expected_result = 1

    result = task_func(date_str, from_tz, to_tz)

    assert result == expected_result

    # Test case 3: Given date is in the same timezone as the destination timezone
    date_str = "2022-01-01 12:00:00"
    from_tz = "America/New_York"
    to_tz = "America/New_York"
    expected_result = 0

    result = task_func(date_str, from_tz, to_tz)

    assert result == expected_result

    # Test case 4: Given date is in a different timezone than the destination timezone
    date_str = "2022-01-01 12:00:00"
    from_tz = "UTC"
    to_tz = "Asia/Tokyo"
    expected_result = 1

    result = task_func(date_str, from_tz, to_tz)

    assert result == expected_result