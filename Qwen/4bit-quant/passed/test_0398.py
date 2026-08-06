import pytest
from src_0398 import task_func

# Mocking urllib.request.urlopen to simulate API responses
from unittest.mock import patch

def test_task_func_valid_ip():
    # Simulate a valid IP response
    mock_response = '{"ip": "192.168.1.1"}'
    with patch('urllib.request.urlopen', return_value=mock_response):
        result = task_func('http://example.com/api')
        assert result == '192.168.1.1'

def test_task_func_invalid_ip():
    # Simulate an invalid IP response
    mock_response = '{"ip": "invalid_ip"}'
    with patch('urllib.request.urlopen', return_value=mock_response):
        result = task_func('http://example.com/api')
        assert result == 'Invalid IP address received'

def test_task_func_exception():
    # Simulate an exception during API request
    with patch('urllib.request.urlopen', side_effect=Exception('Connection error')):
        result = task_func('http://example.com/api')
        assert result == 'Connection error'