import pytest
from src_0321 import task_func
import os
import random
import subprocess

# Mocking subprocess.Popen to avoid actual process execution
class MockPopen:
    def __init__(self, *args, **kwargs):
        self.returncode = random.randint(0, 1)  # Random exit code for mock

    def wait(self):
        pass

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'Popen', MockPopen)

def test_task_func_with_empty_file_list(mock_subprocess):
    directory = '/path/to/directory'
    file_list = []
    result = task_func(directory, file_list)
    assert result is None

def test_task_func_with_non_empty_file_list(mock_subprocess):
    directory = '/path/to/directory'
    file_list = ['file1.txt', 'file2.txt']
    result = task_func(directory, file_list)
    assert result in [0, 1]  # Assuming random return code is either 0 or 1

def test_task_func_with_nonexistent_file(mock_subprocess, monkeypatch):
    directory = '/path/to/directory'
    file_list = ['nonexistent_file.txt']
    
    def mock_os_path_exists(path):
        return False
    
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    
    result = task_func(directory, file_list)
    assert result is None

def test_task_func_with_existing_file(mock_subprocess, monkeypatch):
    directory = '/path/to/directory'
    file_list = ['existing_file.txt']
    
    def mock_os_path_exists(path):
        return True
    
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    
    result = task_func(directory, file_list)
    assert result in [0, 1]  # Assuming random return code is either 0 or 1