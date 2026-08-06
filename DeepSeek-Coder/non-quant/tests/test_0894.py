import pytest
from src_0894 import task_func

def test_task_func():
    logs = [
        "2023-04-01 12:34:56 ERROR Something went wrong",
        "2023-04-01 12:34:57 ERROR Something went wrong",
        "2023-04-01 12:34:58 ERROR Something went wrong"
    ]
    expected_error_times = [time(12, 34)]
    expected_avg_time = time(12, 34)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time