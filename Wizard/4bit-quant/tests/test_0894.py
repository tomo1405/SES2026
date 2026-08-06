python
import pytest
from src_0894 import task_func

def test_task_func():
    logs = [
        "2021-01-01 01:00:00 ERROR Something went wrong",
        "2021-01-01 02:00:00 INFO Finished successfully",
        "2021-01-01 03:00:00 ERROR Something went wrong again",
        "2021-01-01 04:00:00 INFO Finished again successfully",
    ]
    expected_error_times = [time(1, 0), time(3, 0)]
    expected_avg_time = time(2, 0)

    error_times, avg_time = task_func(logs)

    assert error_times == expected_error_times
    assert avg_time == expected_avg_time