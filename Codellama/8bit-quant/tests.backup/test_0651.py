import pytest
from src_0651 import task_func

def test_task_func():
    date_str = "2022-01-01 00:00:00"
    tz_str = "America/New_York"
    expected_result = 82800

    result = task_func(date_str, tz_str)

    assert result == expected_result