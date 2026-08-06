import pytest
from src_0013 import task_func
import os
import json
from datetime import datetime

def test_task_func_default_parameters():
    # Mock the subprocess call and file operations
    def mock_subprocess_call(args):
        return 0

    def mock_open(*args, **kwargs):
        class MockFile:
            def write(self, data):
                pass
        return MockFile()

    monkeypatch.setattr(subprocess, 'call', mock_subprocess_call)
    monkeypatch.setattr('builtins.open', mock_open)

    # Ensure the default log file does not exist before running the test
    if os.path.exists('/home/user/backup_log.json'):
        os.remove('/home/user/backup_log.json')

    result = task_func()

    assert isinstance(result, dict)
    assert 'start_time' in result
    assert 'end_time' in result
    assert 'exit_status' in result
    assert result['exit_status'] == 0

    # Check if the log file was created
    assert os.path.exists('/home/user/backup_log.json')

    # Clean up the log file after the test
    os.remove('/home/user/backup_log.json')

def test_task_func_custom_script_and_log_file(monkeypatch):
    # Mock the subprocess call and file operations
    def mock_subprocess_call(args):
        return 0

    def mock_open(*args, **kwargs):
        class MockFile:
            def write(self, data):
                pass
        return MockFile()

    monkeypatch.setattr(subprocess, 'call', mock_subprocess_call)
    monkeypatch.setattr('builtins.open', mock_open)

    # Define custom script and log file paths
    custom_script = '/path/to/custom_script.sh'
    custom_log_file = '/path/to/custom_log.json'

    # Ensure the custom log file does not exist before running the test
    if os.path.exists(custom_log_file):
        os.remove(custom_log_file)

    result = task_func(script_name=custom_script, log_file=custom_log_file)

    assert isinstance(result, dict)
    assert 'start_time' in result
    assert 'end_time' in result
    assert 'exit_status' in result
    assert result['exit_status'] == 0

    # Check if the custom log file was created
    assert os.path.exists(custom_log_file)

    # Clean up the custom log file after the test
    os.remove(custom_log_file)

def test_task_func_script_not_found(monkeypatch):
    # Mock the subprocess call and file operations
    def mock_subprocess_call(args):
        return 0

    def mock_open(*args, **kwargs):
        class MockFile:
            def write(self, data):
                pass
        return MockFile()

    monkeypatch.setattr(subprocess, 'call', mock_subprocess_call)
    monkeypatch.setattr('builtins.open', mock_open)

    # Define a non-existent script path
    non_existent_script = '/path/to/non_existent_script.sh'

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(script_name=non_existent_script)

    assert str(excinfo.value) == f"Script {non_existent_script} does not exist."