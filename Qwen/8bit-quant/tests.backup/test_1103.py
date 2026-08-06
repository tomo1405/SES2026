import pytest
from src_1103 import task_func
from unittest.mock import patch, Mock
from datetime import datetime

@patch('subprocess.Popen')
@patch('datetime.datetime')
def test_task_func(mock_datetime, mock_popen):
    # Mock datetime.now() to return fixed values
    mock_datetime.now.side_effect = [datetime(2023, 1, 1, 12, 0, 0), datetime(2023, 1, 1, 12, 1, 0)]
    
    # Mock Popen to simulate script execution
    mock_process = Mock()
    mock_process.communicate.return_value = (b'stdout', b'stderr')
    mock_popen.return_value = mock_process
    
    # Call the function with a dummy script path
    result = task_func('/path/to/script.R')
    
    # Assert the expected output
    assert result == {
        'Start Time': '2023-01-01 12:00:00',
        'End Time': '2023-01-01 12:01:00',
        'Stdout': 'stdout',
        'Stderr': 'stderr'
    }

@patch('subprocess.Popen')
@patch('datetime.datetime')
def test_task_func_with_error(mock_datetime, mock_popen):
    # Mock datetime.now() to return fixed values
    mock_datetime.now.side_effect = [datetime(2023, 1, 1, 12, 0, 0), datetime(2023, 1, 1, 12, 1, 0)]
    
    # Mock Popen to simulate script execution with error
    mock_process = Mock()
    mock_process.communicate.return_value = (b'', b'error message')
    mock_popen.return_value = mock_process
    
    # Call the function with a dummy script path
    result = task_func('/path/to/script.R')
    
    # Assert the expected output
    assert result == {
        'Start Time': '2023-01-01 12:00:00',
        'End Time': '2023-01-01 12:01:00',
        'Stdout': '',
        'Stderr': 'error message'
    }

@patch('subprocess.Popen')
def test_task_func_with_no_output(mock_popen):
    # Mock Popen to simulate script execution with no output
    mock_process = Mock()
    mock_process.communicate.return_value = (b'', b'')
    mock_popen.return_value = mock_process
    
    # Call the function with a dummy script path
    result = task_func('/path/to/script.R')
    
    # Assert the expected output
    assert result['Stdout'] == ''
    assert result['Stderr'] == ''