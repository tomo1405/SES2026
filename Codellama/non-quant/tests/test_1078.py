import pytest
from src_1078 import task_func

def test_task_func():
    time_strings = ["10/10/10 10:10:10.100", "10/10/10 10:10:10.200"]
    timezone = "UTC"
    expected_result = 0.1

    result = task_func(time_strings, timezone)

    assert result == expected_result

def test_task_func_with_invalid_timezone():
    time_strings = ["10/10/10 10:10:10.100", "10/10/10 10:10:10.200"]
    timezone = "InvalidTimezone"

    with pytest.raises(ValueError):
        task_func(time_strings, timezone)

def test_task_func_with_invalid_time_string():
    time_strings = ["InvalidTimeString", "10/10/10 10:10:10.200"]
    timezone = "UTC"

    with pytest.raises(ValueError):
        task_func(time_strings, timezone)

def test_task_func_with_empty_time_strings():
    time_strings = []
    timezone = "UTC"

    result = task_func(time_strings, timezone)

    assert result == 0.0

def test_task_func_with_single_time_string():
    time_strings = ["10/10/10 10:10:10.100"]
    timezone = "UTC"

    result = task_func(time_strings, timezone)

    assert result == 0.0