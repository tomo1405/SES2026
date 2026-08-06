import pytest
from src_0462 import task_func
import os
import subprocess
import psutil
import time

# Mocking functions
class MockPopen:
    def __init__(self, *args, **kwargs):
        self.pid = 12345

    def terminate(self):
        pass

    def wait(self):
        pass

    def poll(self):
        return None

class MockProcess:
    def __init__(self, pid):
        self.pid = pid

    def is_running(self):
        return True

    def cpu_percent(self, interval=0.05):
        return 10.0

    def memory_info(self):
        return psutil._common.sinfo(rss=1024)

def mock_os_path_exists(path):
    return True

def mock_time_time():
    return 0.0

@pytest.fixture(autouse=True)
def mock_dependencies(monkeypatch):
    monkeypatch.setattr(subprocess, "Popen", MockPopen)
    monkeypatch.setattr(psutil, "Process", MockProcess)
    monkeypatch.setattr(os.path, "exists", mock_os_path_exists)
    monkeypatch.setattr(time, "time", mock_time_time)

def test_task_func_valid_script():
    script_path = "/path/to/script.sh"
    result = task_func(script_path, timeout=1)
    assert isinstance(result, dict)
    assert "CPU Usage" in result
    assert "Memory Usage" in result
    assert result["CPU Usage"] == 10.0
    assert result["Memory Usage"] == 1024

def test_task_func_nonexistent_script():
    script_path = "/path/to/nonexistent_script.sh"
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(script_path)
    assert str(excinfo.value) == f"'{script_path}' does not exist."

def test_task_func_timeout():
    script_path = "/path/to/script.sh"
    result = task_func(script_path, timeout=0.1)
    assert isinstance(result, dict)
    assert "CPU Usage" in result
    assert "Memory Usage" in result
    assert result["CPU Usage"] == 10.0
    assert result["Memory Usage"] == 1024