import pytest
from src_0495 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    epoch_milliseconds = 1632304000000
    seed = 0
    timezones = ["UTC", "US/Eastern", "Australia/Sydney"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-22",
                "time": "00:00:00",
                "timezone": "Australia/Sydney",
            }
        ]
    }
    actual_output = task_func(epoch_milliseconds, seed, timezones)
    assert actual_output == expected_output

    # Test case 2: Test with invalid input (empty timezones list)
    epoch_milliseconds = 1632304000000
    seed = 0
    timezones = []
    expected_output = {
        "John": [
            {
                "date": "2021-09-22",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    actual_output = task_func(epoch_milliseconds, seed, timezones)
    assert actual_output == expected_output

    # Test case 3: Test with invalid input (invalid timezones)
    epoch_milliseconds = 1632304000000
    seed = 0
    timezones = ["UTC", "Invalid timezone", "Another invalid timezone"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-22",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    actual_output = task_func(epoch_milliseconds, seed, timezones)
    assert actual_output == expected_output