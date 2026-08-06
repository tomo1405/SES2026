import time

from src_0894 import task_func


def test_task_func():
    logs = ["ERROR: 12:30:00", "ERROR: 13:45:00", "ERROR: 14:15:00"]
    error_times, avg_time = task_func(logs)
    assert error_times == [time(12, 30), time(13, 45), time(14, 15)]
    assert avg_time == time(13, 30)

def test_task_func_no_errors():
    logs = ["INFO: 12:30:00", "INFO: 13:45:00", "INFO: 14:15:00"]
    error_times, avg_time = task_func(logs)
    assert error_times == []
    assert avg_time == time(0, 0)

def test_task_func_invalid_logs():
    logs = ["ERROR: 12:30:00", "ERROR: 13:45:00", "ERROR: 14:15:00", "INFO: 15:15:00"]
    error_times, avg_time = task_func(logs)
    assert error_times == [time(12, 30), time(13, 45), time(14, 15)]
    assert avg_time == time(13, 30)