import pytest
from src_1106 import task_func
import os
import subprocess
import time
import glob

# Mocking subprocess module
class MockSubprocess:
    @staticmethod
    def call(command, shell=True):
        pass

# Mocking glob module
class MockGlob:
    @staticmethod
    def glob(pattern):
        pass

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'call', MockSubprocess.call)

@pytest.fixture
def mock_glob(monkeypatch):
    monkeypatch.setattr(glob, 'glob', MockGlob.glob)

def test_task_func_success(mock_subprocess, mock_glob, tmpdir):
    # Create a temporary directory for testing
    r_script_path = tmpdir.join('test_script.R').strpath
    output_path = tmpdir.mkdir('output').strpath
    
    # Mock the glob module to simulate successful file generation
    def mock_glob_success(pattern):
        return [os.path.join(output_path, 'test_output.csv')]
    
    mock_glob.glob = mock_glob_success
    
    # Call the function
    result, message = task_func(r_script_path, output_path, 10)
    
    # Assert the result
    assert result == True
    assert message == 'File generated successfully within the specified duration.'

def test_task_func_failure(mock_subprocess, mock_glob, tmpdir):
    # Create a temporary directory for testing
    r_script_path = tmpdir.join('test_script.R').strpath
    output_path = tmpdir.mkdir('output').strpath
    
    # Mock the glob module to simulate no file generation
    def mock_glob_failure(pattern):
        return []
    
    mock_glob.glob = mock_glob_failure
    
    # Call the function
    result, message = task_func(r_script_path, output_path, 1)
    
    # Assert the result
    assert result == False
    assert message == 'File not generated within the specified duration.'