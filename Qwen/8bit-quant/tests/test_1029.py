import json
import os

import pytest
from src_1029 import task_func


@pytest.fixture
def cleanup_logfile():
    yield
    if os.path.exists("logfile.log"):
        os.remove("logfile.log")

def test_task_func_invalid_interval():
    with pytest.raises(ValueError):
        task_func(-1, 10)

def test_task_func_invalid_duration():
    with pytest.raises(ValueError):
        task_func(1, -10)

def test_task_func_zero_interval():
    with pytest.raises(ValueError):
        task_func(0, 10)

def test_task_func_zero_duration():
    with pytest.raises(ValueError):
        task_func(1, 0)

def test_task_func_positive_values(cleanup_logfile):
    result = task_func(1, 5)
    assert result == "logfile.log"
    assert os.path.exists("logfile.log")

def test_task_func_log_content(cleanup_logfile):
    task_func(1, 3)
    with open("logfile.log", "r", encoding="utf-8") as logfile:
        lines = logfile.readlines()
        assert len(lines) >= 3  # At least 3 entries within 3 seconds

    for line in lines:
        log_data = json.loads(line.strip())
        assert "timestamp" in log_data
        assert "cpu_usage" in log_data
        assert isinstance(log_data["timestamp"], float)
        assert isinstance(log_data["cpu_usage"], str)

def test_task_func_log_timestamps(cleanup_logfile):
    task_func(1, 3)
    with open("logfile.log", "r", encoding="utf-8") as logfile:
        timestamps = [json.loads(line.strip())["timestamp"] for line in logfile.readlines()]
        for i in range(1, len(timestamps)):
            assert timestamps[i] - timestamps[i-1] >= 1  # At least 1 second apart