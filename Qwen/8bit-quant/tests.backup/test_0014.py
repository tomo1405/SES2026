import pytest
from src_0014 import task_func
import ftplib
import os
from unittest.mock import patch, MagicMock

# Mocking the ftplib.FTP class
class MockFTP:
    def __init__(self, *args, **kwargs):
        pass

    def login(self, user, passwd):
        pass

    def cwd(self, dir):
        pass

    def nlst(self):
        return ['file1.txt', 'file2.txt']

    def quit(self):
        pass

# Mocking subprocess.call
def mock_subprocess_call(command, shell):
    pass

@pytest.fixture
def mock_ftp(monkeypatch):
    monkeypatch.setattr(ftplib, 'FTP', MockFTP)

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'call', mock_subprocess_call)

def test_task_func(mock_ftp, mock_subprocess):
    # Test with default parameters
    result = task_func()
    assert result == ['file1.txt', 'file2.txt']
    assert os.path.exists('downloaded_files')
    assert os.listdir('downloaded_files') == []

    # Clean up the created directory
    os.rmdir('downloaded_files')