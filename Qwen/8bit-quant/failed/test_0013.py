import pytest
from src_0013 import task_func
import os
import json
from datetime import datetime

def test_task_func_default_arguments():
    # Mock the subprocess call and file operations
    def mock_subprocess_call(args):
        return 0

    def mock_open(*args, **kwargs):
        class MockFile:
            def write(self, data):
                pass

        return MockFile()

    subprocess.call = mock_subprocess_call
    open = mock_open

    # Call the function
    result = task_func()

    # Check the result
    assert isinstance(result, dict)
    assert 'start_time' in result
    assert 'end_time' in result
    assert 'exit_status' in result
    assert result['exit_status'] == 0

def test_task_func_custom_arguments():
    # Mock the subprocess call and file operations
    def mock_subprocess_call(args):
        return 1

    def mock_open(*args, **kwargs):
        class MockFile:
            def write(self, data):
                pass

        return MockFile()

    subprocess.call = mock_subprocess_call
    open = mock_open

    # Call the function with custom arguments
    result = task_func('custom_backup.sh', '/tmp/custom_backup_log.json')

    # Check the result
    assert isinstance(result, dict)
    assert 'start_time' in result
    assert 'end_time' in result
    assert 'exit_status' in result
    assert result['exit_status'] == 1

def test_task_func_script_not_found():
    # Mock the os.path.isfile to return False
    def mock_isfile(path):
        return False

    os.path.isfile = mock_isfile

    # Expect FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('nonexistent_script.sh')

    assert str(excinfo.value) == "Script nonexistent_script.sh does not exist."

def test_task_func_runtime_error():
    # Mock the subprocess call to raise an exception
    def mock_subprocess_call(args):
        raise Exception("Simulated error")

    subprocess.call = mock_subprocess_call

    # Expect RuntimeError
    with pytest.raises(RuntimeError) as excinfo:
        task_func()

    assert str(excinfo.value).startswith("Failed to run backup.sh:")