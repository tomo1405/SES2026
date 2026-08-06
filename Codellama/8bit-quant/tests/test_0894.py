import time

from src_0894 import task_func


def test_task_func_empty_logs():
    logs = []
    error_times, avg_time = task_func(logs)
    assert error_times == []
    assert avg_time == time(0, 0)

def test_task_func_single_error():
    logs = ["ERROR: 12:34:56"]
    error_times, avg_time = task_func(logs)
    assert error_times == [time(12, 34)]
    assert avg_time == time(12, 34)

def test_task_func_multiple_errors():
    logs = ["ERROR: 12:34:56", "ERROR: 13:45:00", "ERROR: 14:56:12"]
    error_times, avg_time = task_func(logs)
    assert error_times == [time(12, 34), time(13, 45), time(14, 56)]
    assert avg_time == time(13, 34)

def test_task_func_no_errors():
    logs = ["INFO: 12:34:56", "INFO: 13:45:00", "INFO: 14:56:12"]
    error_times, avg_time = task_func(logs)
    assert error_times == []
    assert avg_time == time(0, 0)