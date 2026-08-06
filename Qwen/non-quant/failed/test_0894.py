import pytest
from src_0894 import task_func

def test_task_func_no_errors():
    logs = [
        "INFO 2023-10-01 12:34:56 Some info message",
        "WARNING 2023-10-01 12:35:57 Some warning message"
    ]
    expected_result = ([], time(0, 0))
    assert task_func(logs) == expected_result

def test_task_func_single_error():
    logs = [
        "ERROR 2023-10-01 12:34:56 Some error message"
    ]
    expected_result = ([time(12, 34)], time(12, 34))
    assert task_func(logs) == expected_result

def test_task_func_multiple_errors():
    logs = [
        "ERROR 2023-10-01 12:34:56 First error message",
        "ERROR 2023-10-01 12:35:57 Second error message",
        "ERROR 2023-10-01 12:36:58 Third error message"
    ]
    expected_result = ([time(12, 34), time(12, 35), time(12, 36)], time(12, 35))
    assert task_func(logs) == expected_result

def test_task_func_errors_with_different_minutes():
    logs = [
        "ERROR 2023-10-01 12:01:56 First error message",
        "ERROR 2023-10-01 12:02:57 Second error message",
        "ERROR 2023-10-01 12:03:58 Third error message"
    ]
    expected_result = ([time(12, 1), time(12, 2), time(12, 3)], time(12, 2))
    assert task_func(logs) == expected_result

def test_task_func_mixed_logs():
    logs = [
        "INFO 2023-10-01 12:34:56 Some info message",
        "ERROR 2023-10-01 12:35:57 First error message",
        "WARNING 2023-10-01 12:36:58 Some warning message",
        "ERROR 2023-10-01 12:37:59 Second error message"
    ]
    expected_result = ([time(12, 35), time(12, 37)], time(12, 36))
    assert task_func(logs) == expected_result

def test_task_func_no_time_in_logs():
    logs = [
        "ERROR 2023-10-01 Some error message without time"
    ]
    expected_result = ([], time(0, 0))
    assert task_func(logs) == expected_result