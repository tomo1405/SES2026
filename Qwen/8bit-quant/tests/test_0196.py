import platform
import subprocess

import pytest
from src_0196 import task_func


# Mocking the subprocess and platform modules for testing
class MockPopen:
    def __init__(self, args, shell):
        self.args = args
        self.shell = shell
        self.returncode = 0

    def poll(self):
        return self.returncode

@pytest.fixture
def mock_platform(monkeypatch):
    def mock_system():
        return 'Linux'  # or 'Darwin', 'Windows' for different cases

    monkeypatch.setattr(platform, 'system', mock_system)

@pytest.fixture
def mock_subprocess(monkeypatch):
    def mock_popen(args, shell):
        return MockPopen(args, shell)

    monkeypatch.setattr(subprocess, 'Popen', mock_popen)

def test_task_func(mock_platform, mock_subprocess):
    url = 'http://example.com'
    returncode = task_func(url)
    assert returncode == 0

def test_task_func_windows(mock_platform, mock_subprocess):
    def mock_system():
        return 'Windows'

    monkeypatch.setattr(platform, 'system', mock_system)
    url = 'http://example.com'
    returncode = task_func(url)
    assert returncode == 0

def test_task_func_macos(mock_platform, mock_subprocess):
    def mock_system():
        return 'Darwin'

    monkeypatch.setattr(platform, 'system', mock_system)
    url = 'http://example.com'
    returncode = task_func(url)
    assert returncode == 0