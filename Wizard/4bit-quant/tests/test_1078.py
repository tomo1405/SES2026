python
import pytest
from src_1078 import task_func

def test_task_func():
    time_strings = ["01/01/1970 00:00:00.000", "01/01/1970 00:00:01.000"]
    timezone = "US/Eastern"
    expected_result = 1.0

    result = task_func(time_strings, timezone)

    assert result == expected_result