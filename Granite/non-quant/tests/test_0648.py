import pytest
from src_0648 import task_func


def test_task_func():
    # Test case 1: Convert a date string from one timezone to another
    result = task_func("2023-01-01 12:00:00", "America/New_York", "Asia/Tokyo")
    expected_result = 32400  # 9 hours
    assert result == expected_result, "Test case 1 failed"

    # Test case 2: Convert a date string from one timezone to another
    result = task_func("2023-01-01 00:00:00", "UTC", "Australia/Sydney")
    expected_result = 39600  # 11 hours
    assert result == expected_result, "Test case 2 failed"

    # Test case 3: Handle an invalid date string
    with pytest.raises(ValueError):
        task_func("2023-01-01", "UTC", "Australia/Sydney")