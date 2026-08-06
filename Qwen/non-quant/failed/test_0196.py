import pytest
from src_0196 import task_func
import platform
import subprocess
import os

def test_task_func_darwin(mocker):
    # Mock platform.system to return 'Darwin'
    mocker.patch('platform.system', return_value='Darwin')
    
    # Mock subprocess.Popen to avoid opening a real process
    mock_popen = mocker.patch('subprocess.Popen')
    mock_process = mocker.Mock()
    mock_popen.return_value = mock_process
    
    # Mock process.poll to simulate process completion
    mock_process.poll.side_effect = [None, 0]
    
    # Call the function
    result = task_func('http://example.com')
    
    # Asserts
    assert mock_popen.called_once_with(['open', 'http://example.com'], shell=True)
    assert mock_process.poll.call_count == 2
    assert result == 0

def test_task_func_windows(mocker):
    # Mock platform.system to return 'Windows'
    mocker.patch('platform.system', return_value='Windows')
    
    # Mock subprocess.Popen to avoid opening a real process
    mock_popen = mocker.patch('subprocess.Popen')
    mock_process = mocker.Mock()
    mock_popen.return_value = mock_process
    
    # Mock process.poll to simulate process completion
    mock_process.poll.side_effect = [None, 0]
    
    # Call the function
    result = task_func('http://example.com')
    
    # Asserts
    assert mock_popen.called_once_with(['start', 'http://example.com'], shell=True)
    assert mock_process.poll.call_count == 2
    assert result == 0

def test_task_func_other(mocker):
    # Mock platform.system to return something other than 'Darwin' or 'Windows'
    mocker.patch('platform.system', return_value='Linux')
    
    # Mock subprocess.Popen to avoid opening a real process
    mock_popen = mocker.patch('subprocess.Popen')
    mock_process = mocker.Mock()
    mock_popen.return_value = mock_process
    
    # Mock process.poll to simulate process completion
    mock_process.poll.side_effect = [None, 0]
    
    # Call the function
    result = task_func('http://example.com')
    
    # Asserts
    assert mock_popen.called_once_with(['xdg-open', 'http://example.com'], shell=True)
    assert mock_process.poll.call_count == 2
    assert result == 0

def test_task_func_process_failure(mocker):
    # Mock platform.system to return 'Darwin'
    mocker.patch('platform.system', return_value='Darwin')
    
    # Mock subprocess.Popen to avoid opening a real process
    mock_popen = mocker.patch('subprocess.Popen')
    mock_process = mocker.Mock()
    mock_popen.return_value = mock_process
    
    # Mock process.poll to simulate process failure
    mock_process.poll.side_effect = [None, 1]
    
    # Call the function
    result = task_func('http://example.com')
    
    # Asserts
    assert mock_popen.called_once_with(['open', 'http://example.com'], shell=True)
    assert mock_process.poll.call_count == 2
    assert result == 1