import pytest
from src_0495 import task_func


def test_task_func_valid_input():
    epoch_milliseconds = 1640995200000
    seed = 0
    timezones = ["UTC"]
    expected_output = {
        "event_name": "Alice",
        "date": "2022-01-01",
        "time": "12:00:00",
        "timezone": "UTC",
    }
    assert task_func(epoch_milliseconds, seed, timezones) == expected_output


def test_task_func_invalid_input():
    epoch_milliseconds = 1640995200000
    seed = 0
    timezones = ["Invalid"]
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, seed, timezones)


def test_task_func_invalid_timezone():
    epoch_milliseconds = 1640995200000
    seed = 0
    timezones = ["UTC", "Invalid"]
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, seed, timezones)


def test_task_func_invalid_seed():
    epoch_milliseconds = 1640995200000
    seed = -1
    timezones = ["UTC"]
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, seed, timezones)


def test_task_func_invalid_epoch_milliseconds():
    epoch_milliseconds = -1
    seed = 0
    timezones = ["UTC"]
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, seed, timezones)