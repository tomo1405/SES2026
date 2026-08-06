import time

from src_0894 import task_func


def test_task_func():
    logs = ["ERROR 12:30:00", "INFO 13:45:00", "ERROR 14:10:00", "WARNING 15:20:00"]
    expected_error_times = [time(12, 30), time(14, 10)]
    expected_avg_time = time(13, 10)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time