from unittest.mock import patch

import pytest
import requests
from src_0997 import task_func


@patch('requests.get')
@patch('json.dumps')
@patch('builtins.open')
def test_task_func(mock_open, mock_json_dumps, mock_requests_get):
    # Mock the response from requests.get
    mock_response = mock_requests_get.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><head><title>Test Title</title></head><body></body></html>"
    
    # Mock the behavior of json.dumps
    mock_json_dumps.return_value = '{"title": "Test Title"}'
    
    # Mock the behavior of open
    mock_file = mock_open.return_value.__enter__.return_value
    
    # Call the function
    result = task_func("http://example.com")
    
    # Assertions
    assert result == "Output.txt"
    mock_requests_get.assert_called_once_with("http://example.com", timeout=5)
    mock_json_dumps.assert_called_once_with({"title": "Test Title"})
    mock_file.write.assert_called_once_with('{"title": "Test Title"}\n')

@patch('requests.get', side_effect=requests.exceptions.RequestException)
def test_task_func_request_exception(mock_requests_get):
    # Call the function
    with pytest.raises(requests.exceptions.RequestException):
        task_func("http://example.com")

@patch('requests.get', return_value=mock.Mock(status_code=404))
def test_task_func_non_200_status(mock_requests_get):
    # Call the function
    with pytest.raises(Exception) as excinfo:
        task_func("http://example.com")
    assert str(excinfo.value) == "HTTP Error 404: Not Found"

@patch('requests.get', return_value=mock.Mock(status_code=200, text="<html><head></head><body></body></html>"))
def test_task_func_no_title(mock_requests_get):
    # Call the function
    result = task_func("http://example.com")
    
    # Assertions
    assert result == "Output.txt"
    mock_requests_get.assert_called_once_with("http://example.com", timeout=5)