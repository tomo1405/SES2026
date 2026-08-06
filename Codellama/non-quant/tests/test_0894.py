import time

from src_0894 import task_func


def test_task_func():
    logs = [
        "ERROR: 2022-02-22 12:34:56",
        "INFO: 2022-02-22 13:45:07",
        "ERROR: 2022-02-22 14:56:18",
        "INFO: 2022-02-22 15:07:29",
        "ERROR: 2022-02-22 16:18:30",
    ]
    expected_error_times = [time(12, 34), time(14, 56), time(16, 18)]
    expected_avg_time = time(14, 28)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time