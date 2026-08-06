import re
from datetime import time
from src_0894 import task_func
import pytest

def test_task_func():
    logs = ["ERROR 12:30:00", "ERROR 13:45:00", "INFO 14:00:00"]
    expected_error_times = [time(12, 30), time(13, 45)]
    expected_avg_time = time(13, 12)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time

def test_task_func_with_no_errors():
    logs = ["INFO 12:30:00", "INFO 13:45:00", "INFO 14:00:00"]
    expected_error_times = []
    expected_avg_time = time(0, 0)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time