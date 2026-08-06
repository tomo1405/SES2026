import pytest
from src_0894 import task_func

def test_task_func_no_errors():
    logs = [
        "INFO 2023-10-01 12:30:45 - Starting process",
        "DEBUG 2023-10-01 12:35:10 - Process running smoothly",
        "INFO 2023-10-01 12:40:20 - Process completed"
    ]
    expected_output = ([], time(0, 0))
    assert task_func(logs) == expected_output

def test_task_func_single_error():
    logs = [
        "ERROR 2023-10-01 12:30:45 - Something went wrong",
        "INFO 2023-10-01 12:35:10 - Process running smoothly",
        "INFO 2023-10-01 12:40:20 - Process completed"
    ]
    expected_output = ([time(12, 30)], time(12, 30))
    assert task_func(logs) == expected_output

def test_task_func_multiple_errors():
    logs = [
        "ERROR 2023-10-01 12:30:45 - Something went wrong",
        "ERROR 2023-10-01 13:45:10 - Another issue",
        "INFO 2023-10-01 12:40:20 - Process completed"
    ]
    expected_output = ([time(12, 30), time(13, 45)], time(13, 7))
    assert task_func(logs) == expected_output

def test_task_func_invalid_time_format():
    logs = [
        "ERROR 2023-10-01 12:30:45 - Something went wrong",
        "ERROR 2023-10-01 13:45:10 - Another issue",
        "ERROR 2023-10-01 14:60:20 - Invalid time"
    ]
    expected_output = ([time(12, 30), time(13, 45)], time(13, 7))
    assert task_func(logs) == expected_output

def test_task_func_all_errors():
    logs = [
        "ERROR 2023-10-01 12:30:45 - Something went wrong",
        "ERROR 2023-10-01 13:45:10 - Another issue",
        "ERROR 2023-10-01 14:15:20 - Yet another problem"
    ]
    expected_output = ([time(12, 30), time(13, 45), time(14, 15)], time(13, 20))
    assert task_func(logs) == expected_output