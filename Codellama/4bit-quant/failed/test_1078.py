import pytest
from src_1078 import task_func

def test_task_func():
    time_strings = ["10/10/10 10:10:10.100", "11/11/11 11:11:11.110"]
    timezone = "UTC"
    expected_result = 0.0
    assert task_func(time_strings, timezone) == expected_result

def test_task_func_with_invalid_time_strings():
    time_strings = ["invalid_time_string"]
    timezone = "UTC"
    expected_result = 0.0
    assert task_func(time_strings, timezone) == expected_result

def test_task_func_with_empty_time_strings():
    time_strings = []
    timezone = "UTC"
    expected_result = 0.0
    assert task_func(time_strings, timezone) == expected_result

def test_task_func_with_multiple_time_strings():
    time_strings = ["10/10/10 10:10:10.100", "11/11/11 11:11:11.110", "12/12/12 12:12:12.120"]
    timezone = "UTC"
    expected_result = 1.0
    assert task_func(time_strings, timezone) == expected_result