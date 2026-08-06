import pytest
from src_1130 import task_func
import json
import os
from unittest.mock import patch, mock_open

@patch('src_1130.requests.get')
@patch('src_1130.datetime')
@patch('src_1130.os.getcwd')
def test_task_func(mock_getcwd, mock_datetime, mock_requests_get):
    # Mocking the current working directory
    mock_getcwd.return_value = '/tmp'
    
    # Mocking the datetime to return a fixed timestamp
    mock_now = mock_datetime.now.return_value
    mock_now.strftime.return_value = "20230401123456789012"
    
    # Mocking the response content
    mock_response = mock_requests_get.return_value
    mock_response.content = b"Mocked response content"
    
    # JSON data containing the URL
    json_data = '{"url": "http://example.com"}'
    
    # Calling the function
    result = task_func(json_data, "url", "/test/save/dir")
    
    # Expected file path
    expected_file_path = "/test/save/dir/url_20230401123456789012.txt"
    
    # Assertions
    assert result == expected_file_path
    
    # Verify that the file was written correctly
    with open(expected_file_path, 'rb') as f:
        content = f.read()
        assert content == b"Mocked response content"
    
    # Verify that the correct URL was requested
    mock_requests_get.assert_called_once_with("http://example.com")

@patch('src_1130.requests.get')
@patch('src_1130.datetime')
def test_task_func_no_save_dir(mock_datetime, mock_requests_get):
    # Mocking the datetime to return a fixed timestamp
    mock_now = mock_datetime.now.return_value
    mock_now.strftime.return_value = "20230401123456789012"
    
    # Mocking the response content
    mock_response = mock_requests_get.return_value
    mock_response.content = b"Mocked response content"
    
    # JSON data containing the URL
    json_data = '{"url": "http://example.com"}'
    
    # Calling the function without specifying save_dir
    result = task_func(json_data, "url")
    
    # Expected file path (using current working directory)
    expected_file_path = os.path.join(os.getcwd(), "url_20230401123456789012.txt")
    
    # Assertions
    assert result == expected_file_path
    
    # Verify that the file was written correctly
    with open(expected_file_path, 'rb') as f:
        content = f.read()
        assert content == b"Mocked response content"
    
    # Verify that the correct URL was requested
    mock_requests_get.assert_called_once_with("http://example.com")