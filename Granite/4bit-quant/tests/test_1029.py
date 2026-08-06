import json

import pytest
from src_1029 import task_func

LOGFILE_PATH = "logfile.log"
def test_task_func():
    interval = 1
    duration = 5
    result = task_func(interval, duration)
    assert result == LOGFILE_PATH
    with open(LOGFILE_PATH, "r", encoding="utf-8") as logfile:
        lines = logfile.readlines()
        assert len(lines) >= 5
        for line in lines:
            log_data = json.loads(line)
            assert "timestamp" in log_data
            assert "cpu_usage" in log_data
            assert isinstance(log_data["timestamp"], float)
            assert isinstance(log_data["cpu_usage"], str)
def test_task_func_invalid_interval():
    interval = 0
    duration = 5
    with pytest.raises(ValueError) as excinfo:
        task_func(interval, duration)
    assert "Interval and duration must be greater than zero." in str(excinfo.value)
def test_task_func_invalid_duration():
    interval = 1
    duration = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(interval, duration)
    assert "Interval and duration must be greater than zero." in str(excinfo.value)
def test_task_func_invalid_input():
    interval = "invalid"
    duration = "invalid"
    with pytest.raises(TypeError) as excinfo:
        task_func(interval, duration)
    assert "interval must be a number" in str(excinfo.value)
    assert "duration must be a number" in str(excinfo.value)