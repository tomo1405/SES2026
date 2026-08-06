import pytest
from src_0495 import task_func

def test_task_func():
    epoch_milliseconds = 1643230400000
    seed = 0
    timezones = ["UTC"]
    expected_event_schedule = {
        "event_name": [
            {
                "date": "2022-02-01",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_event_schedule

def test_task_func_with_invalid_timezones():
    epoch_milliseconds = 1643230400000
    seed = 0
    timezones = ["Invalid"]
    expected_event_schedule = {
        "event_name": [
            {
                "date": "2022-02-01",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_event_schedule

def test_task_func_with_multiple_timezones():
    epoch_milliseconds = 1643230400000
    seed = 0
    timezones = ["UTC", "America/New_York"]
    expected_event_schedule = {
        "event_name": [
            {
                "date": "2022-02-01",
                "time": "00:00:00",
                "timezone": "UTC",
            },
            {
                "date": "2022-02-01",
                "time": "00:00:00",
                "timezone": "America/New_York",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_event_schedule

def test_task_func_with_invalid_seed():
    epoch_milliseconds = 1643230400000
    seed = "Invalid"
    timezones = ["UTC"]
    expected_event_schedule = {
        "event_name": [
            {
                "date": "2022-02-01",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_event_schedule

def test_task_func_with_invalid_epoch_milliseconds():
    epoch_milliseconds = "Invalid"
    seed = 0
    timezones = ["UTC"]
    expected_event_schedule = {
        "event_name": [
            {
                "date": "2022-02-01",
                "time": "00:00:00",
                "timezone": "UTC",
            }
        ]
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_event_schedule