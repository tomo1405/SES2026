import pytest
from src_1075 import task_func

def test_task_func():
    # Test case 1:
    time_string = "01/01/2023 12:00:00.000"
    from_tz = "UTC"
    to_tz = "America/New_York"
    expected_result = "01/01/2023 07:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 2:
    time_string = "01/01/2023 12:00:00.000"
    from_tz = "UTC"
    to_tz = "Asia/Tokyo"
    expected_result = "01/01/2023 19:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 3:
    time_string = "01/01/2023 12:00:00.000"
    from_tz = "UTC"
    to_tz = "Europe/London"
    expected_result = "01/01/2023 13:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 4:
    time_string = "01/01/2023 12:00:00.000"
    from_tz = "UTC"
    to_tz = "Australia/Sydney"
    expected_result = "01/01/2023 20:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result

    # Test case 5:
    time_string = "01/01/2023 12:00:00.000"
    from_tz = "UTC"
    to_tz = "America/Los_Angeles"
    expected_result = "01/01/2023 05:00:00.000"
    assert task_func(time_string, from_tz, to_tz) == expected_result