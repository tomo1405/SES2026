import pytest
from src_0648 import task_func

def test_task_func():
    # Test case 1: Convert a date from one timezone to another
    date_str = "2023-03-14 12:00:00"
    from_tz = "America/New_York"
    to_tz = "Asia/Tokyo"
    expected_output = 10800  # 3 hours in seconds
    actual_output = task_func(date_str, from_tz, to_tz)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: Check if the function raises an exception for an invalid date string
    date_str = "invalid_date"
    with pytest.raises(ValueError):
        task_func(date_str, from_tz, to_tz)

    # Test case 3: Check if the function returns the correct time difference for a future date
    date_str = "2023-03-15 12:00:00"
    expected_output = 86400  # 24 hours in seconds
    actual_output = task_func(date_str, from_tz, to_tz)
    assert actual_output == expected_output, "Test case 3 failed"