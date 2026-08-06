import pytest
from src_0651 import task_func

def test_task_func():
    # Test case 1: Given date is in the same timezone as the New Year moment
    date_str = "2022-01-01 00:00:00"
    tz_str = "America/New_York"
    expected_result = 82800
    assert task_func(date_str, tz_str) == expected_result

    # Test case 2: Given date is in a different timezone than the New Year moment
    date_str = "2022-01-01 00:00:00"
    tz_str = "Europe/London"
    expected_result = 86400
    assert task_func(date_str, tz_str) == expected_result

    # Test case 3: Given date is in a different timezone than the New Year moment, but the New Year moment is in the same timezone as the given date
    date_str = "2022-01-01 00:00:00"
    tz_str = "America/New_York"
    expected_result = 82800
    assert task_func(date_str, tz_str) == expected_result

    # Test case 4: Given date is in a different timezone than the New Year moment, and the New Year moment is in a different timezone than the given date
    date_str = "2022-01-01 00:00:00"
    tz_str = "Europe/London"
    expected_result = 86400
    assert task_func(date_str, tz_str) == expected_result

    # Test case 5: Given date is in a different timezone than the New Year moment, and the New Year moment is in a different timezone than the given date, but the New Year moment is in the same timezone as the given date
    date_str = "2022-01-01 00:00:00"
    tz_str = "America/New_York"
    expected_result = 82800
    assert task_func(date_str, tz_str) == expected_result

    # Test case 6: Given date is in a different timezone than the New Year moment, and the New Year moment is in a different timezone than the given date, and the New Year moment is in a different timezone than the given date
    date_str = "2022-01-01 00:00:00"
    tz_str = "Europe/London"
    expected_result = 86400
    assert task_func(date_str, tz_str) == expected_result