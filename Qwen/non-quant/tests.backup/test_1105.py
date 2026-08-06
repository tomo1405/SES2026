import pytest
from src_1105 import task_func
import os
import subprocess
import threading

# Mocking subprocess and os modules for testing
class MockSubprocess:
    @staticmethod
    def call(args):
        pass

class MockOs:
    @staticmethod
    def system(command):
        pass

@pytest.fixture(autouse=True)
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'call', MockSubprocess.call)

@pytest.fixture(autouse=True)
def mock_os(monkeypatch):
    monkeypatch.setattr(os, 'system', MockOs.system)

def test_task_func_success(mocker):
    script_path = "test_script.py"
    timeout = 60

    # Mock the thread join to simulate successful execution within timeout
    def mock_join(self, timeout=None):
        self._is_alive = False

    mocker.patch.object(threading.Thread, 'join', mock_join)

    result = task_func(script_path, timeout)
    assert result == 'Script executed successfully.'

def test_task_func_timeout(mocker):
    script_path = "test_script.py"
    timeout = 60

    # Mock the thread join to simulate a timeout
    def mock_join(self, timeout=None):
        self._is_alive = True

    mocker.patch.object(threading.Thread, 'join', mock_join)

    result = task_func(script_path, timeout)
    assert result == 'Terminating process due to timeout.'

def test_task_func_timeout_os_system_called(mocker):
    script_path = "test_script.py"
    timeout = 60

    # Mock the thread join to simulate a timeout
    def mock_join(self, timeout=None):
        self._is_alive = True

    mocker.patch.object(threading.Thread, 'join', mock_join)

    # Spy on os.system to ensure it's called
    spy = mocker.spy(os, 'system')

    task_func(script_path, timeout)
    spy.assert_called_once_with(f'pkill -f "{script_path}"')