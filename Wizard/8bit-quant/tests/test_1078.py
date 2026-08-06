python
import pytest
from src_1078 import task_func

def test_task_func():
    time_strings = ["01/01/19 00:00:00.000", "01/01/19 00:00:01.000", "01/01/19 00:00:02.000"]
    timezone = "US/Eastern"
    expected_result = 1.0
    assert task_func(time_strings, timezone) == expected_result