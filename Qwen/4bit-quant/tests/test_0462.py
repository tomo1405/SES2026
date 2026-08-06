import pytest
from src_0462 import task_func
import os
import subprocess
import psutil
import time

# Mocking dependencies
class MockProcess:
    def __init__(self, pid):
        self.pid = pid
        self._is_running = True

    def cpu_percent(self, interval=0.05):
        return 10.0

    def memory_info(self):
        return psutil.virtual_memory()

    def is_running(self):
        return self._is_running

    def terminate(self):
        self._is_running = False

    def wait(self):
        pass

def mock_subprocess_popen(monkeypatch, pid):
    class MockPopen:
        def __init__(self, args):
            self.pid = pid

        def poll(self):
            return None

    monkeypatch.setattr(subprocess, 'Popen', MockPopen)

def test_task_func_timeout(monkeypatch):
    script_path = "/path/to/script.sh"
    mock_pid = 12345
    mock_subprocess_popen(monkeypatch, mock_pid)
    monkeypatch.setattr(psutil, 'Process', lambda pid: MockProcess(pid))

    result = task_func(script_path, timeout=1)
    assert isinstance(result, dict)
    assert "CPU Usage" in result
    assert "Memory Usage" in result

def test_task_func_script_not_found():
    script_path = "/nonexistent/path.sh"
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(script_path)
    assert str(excinfo.value) == f"'{script_path}' does not exist."

def test_task_func_process_terminated(monkeypatch):
    script_path = "/path/to/script.sh"
    mock_pid = 12345
    mock_subprocess_popen(monkeypatch, mock_pid)
    monkeypatch.setattr(psutil, 'Process', lambda pid: MockProcess(pid))

    class MockProcessTerminated(MockProcess):
        def __init__(self, pid):
            super().__init__(pid)
            self._is_running = False

    monkeypatch.setattr(psutil, 'Process', lambda pid: MockProcessTerminated(pid))

    result = task_func(script_path)
    assert isinstance(result, dict)
    assert "CPU Usage" in result
    assert "Memory Usage" in result