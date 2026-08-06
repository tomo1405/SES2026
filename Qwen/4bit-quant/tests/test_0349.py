import pytest
from src_0349 import task_func
import subprocess
import os
import signal
import time

# Mocking subprocess.check_output to simulate different scenarios
class MockSubprocess:
    def __init__(self, output):
        self.output = output

    def check_output(self, args):
        if args == ['pgrep', '-f', 'non_existent_process']:
            raise subprocess.CalledProcessError(1, args)
        elif args == ['pgrep', '-f', 'existing_process']:
            return self.output.encode()

# Patching os.kill to simulate process termination
def mock_os_kill(pid, sig):
    pass

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'check_output', MockSubprocess('1234\n5678').check_output)

@pytest.fixture
def mock_os_kill(monkeypatch):
    monkeypatch.setattr(os, 'kill', mock_os_kill)

def test_task_func_no_processes_found(mock_subprocess, mock_os_kill):
    result = task_func('non_existent_process')
    assert result == 0

def test_task_func_processes_found(mock_subprocess, mock_os_kill):
    result = task_func('existing_process')
    assert result == 2

def test_task_func_with_timeout(monkeypatch):
    def delayed_check_output(args):
        time.sleep(2)
        return b''

    monkeypatch.setattr(subprocess, 'check_output', delayed_check_output)
    monkeypatch.setattr(os, 'kill', mock_os_kill)

    start_time = time.time()
    result = task_func('delayed_process')
    end_time = time.time()

    assert result == 0
    assert (end_time - start_time) >= 1  # Ensure the sleep in task_func is respected