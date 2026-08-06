import pytest
from src_1078 import task_func
from datetime import datetime
import pytz
import numpy as np

def test_task_func():
    time_strings = ["01/01/22 00:00:00.000000", "01/01/22 00:00:01.000000"]
    timezone = "UTC"
    expected_output = 1.0
    actual_output = task_func(time_strings, timezone)
    assert actual_output == expected_output

def test_task_func_with_one_time_string():
    time_strings = ["01/01/22 00:00:00.000000"]
    timezone = "UTC"
    expected_output = 0.0
    actual_output = task_func(time_strings, timezone)
    assert actual_output == expected_output

def test_task_func_with_empty_time_strings():
    time_strings = []
    timezone = "UTC"
    expected_output = 0.0
    actual_output = task_func(time_strings, timezone)
    assert actual_output == expected_output

def test_task_func_with_timezone_not_in_pytz():
    time_strings = ["01/01/22 00:00:00.000000", "01/01/22 00:00:01.000000"]
    timezone = "Invalid_timezone"
    with pytest.raises(pytz.exceptions.UnknownTimeZoneError):
        task_func(time_strings, timezone)