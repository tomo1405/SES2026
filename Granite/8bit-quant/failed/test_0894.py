import pytest
from src_0894 import task_func

def test_task_func():
    logs = ["ERROR 12:34:56", "INFO 13:45:23", "ERROR 14:23:12", "WARNING 15:12:09"]
    expected_error_times = [time(12, 34), time(14, 23)]
    expected_avg_time = time(13, 29)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time

def test_task_func_no_error():
    logs = ["INFO 12:34:56", "INFO 13:45:23", "INFO 14:23:12", "WARNING 15:12:09"]
    expected_error_times = []
    expected_avg_time = time(0, 0)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time

def test_task_func_empty_logs():
    logs = []
    expected_error_times = []
    expected_avg_time = time(0, 0)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time