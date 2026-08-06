import subprocess
import time
import json
import platform
from src_1029 import task_func
import pytest

def test_task_func():
    # Test case 1: interval and duration are both positive
    interval = 1
    duration = 5
    result = task_func(interval, duration)
    assert result == "logfile.log"

    # Test case 2: interval is zero
    interval = 0
    duration = 5
    with pytest.raises(ValueError) as excinfo:
        task_func(interval, duration)
    assert "Interval and duration must be greater than zero." in str(excinfo.value)

    # Test case 3: duration is zero
    interval = 1
    duration = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(interval, duration)
    assert "Interval and duration must be greater than zero." in str(excinfo.value)

    # Test case 4: interval and duration are both negative
    interval = -1
    duration = -5
    with pytest.raises(ValueError) as excinfo:
        task_func(interval, duration)
    assert "Interval and duration must be greater than zero." in str(excinfo.value)