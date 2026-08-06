python
import pytest
from src_0495 import task_func

def test_task_func():
    # Test case 1: Valid input
    epoch_milliseconds = 1631158400000
    seed = 0
    timezones = ["UTC"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-01",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

    # Test case 2: Invalid timezone input
    epoch_milliseconds = 1631158400000
    seed = 0
    timezones = ["Invalid timezone"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-01",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

    # Test case 3: Empty timezone input
    epoch_milliseconds = 1631158400000
    seed = 0
    timezones = []
    expected_output = {
        "John": [
            {
                "date": "2021-09-01",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

    # Test case 4: Multiple valid timezones
    epoch_milliseconds = 1631158400000
    seed = 0
    timezones = ["UTC", "America/New_York", "Asia/Kolkata"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-01",
                "time": "00:00:00",
                "timezone": "Asia/Kolkata",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

    # Test case 5: Multiple valid and invalid timezones
    epoch_milliseconds = 1631158400000
    seed = 0
    timezones = ["UTC", "Invalid timezone", "Asia/Kolkata"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-01",
                "time": "00:00:00",
                "timezone": "Asia/Kolkata",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

    # Test case 6: Multiple valid and empty timezones
    epoch_milliseconds = 1631158400000
    seed = 0
    timezones = ["UTC", "", "Asia/Kolkata"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-01",
                "time": "00:00:00",
                "timezone": "Asia/Kolkata",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

    # Test case 7: Multiple valid and invalid and empty timezones
    epoch_milliseconds = 1631158400000
    seed = 0
    timezones = ["UTC", "Invalid timezone", "", "Asia/Kolkata"]
    expected_output = {
        "John": [
            {
                "date": "2021-09-01",
                "time": "00:00:00",
                "timezone": "Asia/Kolkata",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output