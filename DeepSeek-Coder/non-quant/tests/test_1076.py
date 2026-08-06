import pytest
from src_1076 import task_func

def test_task_func():
    time_strings = [
        "01/01/22 00:00:00.000",
        "01/01/22 00:00:01.000",
        "01/01/22 00:00:02.000"
    ]
    result = task_func(time_strings)
    assert result is not None