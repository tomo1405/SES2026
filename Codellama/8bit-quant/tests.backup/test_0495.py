import pytest
from src_0495 import task_func

def test_task_func_valid_input():
    epoch_milliseconds = 1647187200000
    seed = 0
    timezones = ["UTC"]
    expected_output = {
        "event_name": "Alice",
        "date": "2022-03-14",
        "time": "12:00:00",
        "timezone": "UTC"
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

def test_task_func_invalid_input():
    epoch_milliseconds = 1647187200000
    seed = 0
    timezones = ["Invalid"]
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, seed, timezones)

def test_task_func_random_timezone():
    epoch_milliseconds = 1647187200000
    seed = 0
    timezones = ["UTC", "America/New_York", "Asia/Tokyo"]
    expected_output = {
        "event_name": "Alice",
        "date": "2022-03-14",
        "time": "12:00:00",
        "timezone": "America/New_York"
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output

def test_task_func_random_timezone_with_seed():
    epoch_milliseconds = 1647187200000
    seed = 1
    timezones = ["UTC", "America/New_York", "Asia/Tokyo"]
    expected_output = {
        "event_name": "Alice",
        "date": "2022-03-14",
        "time": "12:00:00",
        "timezone": "Asia/Tokyo"
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output