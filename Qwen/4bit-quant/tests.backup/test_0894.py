import pytest
from src_0894 import task_func

def test_task_func_no_errors():
    logs = [
        "INFO 12:34:56 Some info message",
        "DEBUG 07:23:45 Debugging info",
        "WARNING 15:45:30 Warning message"
    ]
    result = task_func(logs)
    assert result == ([], time(0, 0))

def test_task_func_single_error():
    logs = [
        "ERROR 09:15:30 Something went wrong",
        "INFO 12:34:56 Some info message"
    ]
    result = task_func(logs)
    assert result == ([time(9, 15)], time(9, 15))

def test_task_func_multiple_errors():
    logs = [
        "ERROR 08:30:20 Error one",
        "ERROR 10:45:10 Error two",
        "INFO 12:34:56 Some info message"
    ]
    result = task_func(logs)
    assert result == ([time(8, 30), time(10, 45)], time(9, 37))

def test_task_func_same_minute_errors():
    logs = [
        "ERROR 09:15:30 Error one",
        "ERROR 09:15:45 Error two",
        "INFO 12:34:56 Some info message"
    ]
    result = task_func(logs)
    assert result == ([time(9, 15), time(9, 15)], time(9, 15))

def test_task_func_no_time_in_logs():
    logs = [
        "ERROR Something went wrong",
        "INFO 12:34:56 Some info message"
    ]
    result = task_func(logs)
    assert result == ([], time(0, 0))

def test_task_func_invalid_time_format():
    logs = [
        "ERROR 09-15-30 Error one",
        "ERROR 10:45:10 Error two",
        "INFO 12:34:56 Some info message"
    ]
    result = task_func(logs)
    assert result == ([], time(0, 0))