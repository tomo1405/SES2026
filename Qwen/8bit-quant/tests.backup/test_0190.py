import pytest
from src_0190 import task_func
import requests
from unittest.mock import patch

def test_task_func_valid_url():
    # Mock the requests.get call to return a valid JSON response
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"names": ["Alice", "Bob", "Charlie"]}'
    
    with patch('requests.get', return_value=mock_response):
        result = task_func("http://example.com/data")
        assert result == ['Alice', 'Bob', 'Charlie']

def test_task_func_invalid_url():
    # Mock the requests.get call to raise an exception
    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        result = task_func("http://invalid-url.com/data")
        assert result == "Invalid url input"

def test_task_func_missing_names_key():
    # Mock the requests.get call to return a JSON response without 'names' key
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"other_key": ["Alice", "Bob", "Charlie"]}'
    
    with patch('requests.get', return_value=mock_response):
        result = task_func("http://example.com/data")
        assert result == []

def test_task_func_empty_names_list():
    # Mock the requests.get call to return a JSON response with an empty 'names' list
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"names": []}'
    
    with patch('requests.get', return_value=mock_response):
        result = task_func("http://example.com/data")
        assert result == []