import pytest
from src_0018 import task_func
import subprocess
import psutil
import time

# Mocking psutil and subprocess to control behavior during tests
class MockProcess:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def terminate(self):
        pass

class MockPopen:
    def __init__(self, args):
        self.args = args

    def wait(self):
        pass

def test_task_func_process_not_running(mocker):
    # Mock psutil.process_iter to return no processes
    mocker.patch('psutil.process_iter', return_value=[])
    # Mock subprocess.Popen to simulate starting a process
    mocker.patch('subprocess.Popen', side_effect=MockPopen)

    result = task_func("non_existent_process")
    assert result == "Process not found. Starting non_existent_process."
    subprocess.Popen.assert_called_once_with("non_existent_process")

def test_task_func_process_running(mocker):
    # Mock psutil.process_iter to return a process with the given name
    mock_process = MockProcess("existing_process")
    mocker.patch('psutil.process_iter', return_value=[mock_process])
    # Mock subprocess.Popen to simulate starting a process
    mocker.patch('subprocess.Popen', side_effect=MockPopen)

    result = task_func("existing_process")
    assert result == "Process found. Restarting existing_process."
    mock_process.terminate.assert_called_once()
    time.sleep.assert_called_once_with(5)
    subprocess.Popen.assert_called_once_with("existing_process")