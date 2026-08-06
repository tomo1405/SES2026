import os
import subprocess

import pytest
from src_0811 import task_func


def test_task_func_no_files():
    # Test case where no files match the pattern
    results = task_func('/nonexistent', r'\.txt$')
    assert results == []

def test_task_func_with_files(mock_os_walk, mock_subprocess_run):
    # Mocking os.walk to return a directory with files
    mock_os_walk.return_value = [
        ('/test_dir', [], ['file1.txt', 'file2.exe'])
    ]
    
    # Mocking subprocess.run to simulate successful execution
    mock_subprocess_run.return_value.stdout = b'Hello, World!'
    
    # Test case where files match the pattern and execute_files is True
    results = task_func('/test_dir', r'\.exe$', execute_files=True)
    assert results == ['Hello, World!']

def test_task_func_with_files_no_execute(mock_os_walk):
    # Mocking os.walk to return a directory with files
    mock_os_walk.return_value = [
        ('/test_dir', [], ['file1.txt', 'file2.exe'])
    ]
    
    # Test case where files match the pattern and execute_files is False
    results = task_func('/test_dir', r'\.exe$', execute_files=False)
    assert results == ['/test_dir/file2.exe']

def test_task_func_with_non_executable_files(mock_os_walk):
    # Mocking os.walk to return a directory with files
    mock_os_walk.return_value = [
        ('/test_dir', [], ['file1.txt', 'file2.exe'])
    ]
    
    # Test case where files do not match the pattern
    results = task_func('/test_dir', r'\.bat$')
    assert results == []

# Mocking setup for os.walk and subprocess.run
@pytest.fixture
def mock_os_walk(monkeypatch):
    monkeypatch.setattr(os, 'walk', lambda x: [(x, [], ['file1.txt', 'file2.exe'])])

@pytest.fixture
def mock_subprocess_run(monkeypatch):
    monkeypatch.setattr(subprocess, 'run', lambda x, **kwargs: subprocess.CompletedProcess(args=x, returncode=0, stdout=b'Hello, World!'))