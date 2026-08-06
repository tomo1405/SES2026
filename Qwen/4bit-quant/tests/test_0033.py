from unittest.mock import patch

import requests
from src_0033 import task_func


@patch('requests.get')
def test_task_func(mock_get):
    # Mock the response from requests.get
    mock_response = mock_get.return_value
    mock_response.text = "<html><body><h1>Test Title</h1></body></html>"
    
    # Test case 1: Valid URL and tag
    result = task_func("http://example.com", "h1")
    assert result == "Test Title"
    
    # Test case 2: Tag not found in HTML
    result = task_func("http://example.com", "p")
    assert result is None
    
    # Test case 3: Invalid URL (mocked to return empty text)
    mock_response.text = ""
    result = task_func("http://invalid-url.com", "h1")
    assert result is None

@patch('requests.get')
def test_task_func_with_nonexistent_url(mock_get):
    # Mock the response from requests.get to simulate a non-existent URL
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    
    # Test case: URL returns a 404 error
    result = task_func("http://nonexistent-url.com", "h1")
    assert result is None

@patch('requests.get')
def test_task_func_with_no_internet_connection(mock_get):
    # Mock the response from requests.get to simulate no internet connection
    mock_get.side_effect = requests.exceptions.RequestException
    
    # Test case: No internet connection
    result = task_func("http://example.com", "h1")
    assert result is None