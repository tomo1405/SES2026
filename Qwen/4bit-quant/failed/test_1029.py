import pytest
from src_1029 import task_func
import os
import time
import json

def test_task_func_invalid_interval():
    with pytest.raises(ValueError):
        task_func(-1, 10)

def test_task_func_invalid_duration():
    with pytest.raises(ValueError):
        task_func(1, -1)

def test_task_func_zero_interval():
    with pytest.raises(ValueError):
        task_func(0, 10)

def test_task_func_zero_duration():
    with pytest.raises(ValueError):
        task_func(1, 0)

def test_task_func_valid_input(tmp_path):
    log_file_path = tmp_path / "logfile.log"
    os.environ["LOGFILE_PATH"] = str(log_file_path)
    
    task_func(1, 2)
    
    assert log_file_path.exists()
    
    with open(log_file_path, "r", encoding="utf-8") as logfile:
        lines = logfile.readlines()
        assert len(lines) > 0
        
        for line in lines:
            data = json.loads(line.strip())
            assert "timestamp" in data
            assert "cpu_usage" in data
            assert isinstance(data["timestamp"], float)
            assert isinstance(data["cpu_usage"], str)

def test_task_func_file_write_error(monkeypatch):
    def mock_check_output(*args, **kwargs):
        raise subprocess.CalledProcessError(1, args[0])

    monkeypatch.setattr(subprocess, "check_output", mock_check_output)

    log_file_path = task_func(1, 2)
    assert log_file_path is None

def test_task_func_sleep_time_adjustment(monkeypatch):
    def mock_check_output(*args, **kwargs):
        return b"Mock CPU Usage Data"

    monkeypatch.setattr(subprocess, "check_output", mock_check_output)

    start_time = time.time()
    task_func(0.5, 1)
    end_time = time.time()

    assert end_time - start_time >= 1