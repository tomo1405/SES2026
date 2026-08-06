import pytest
from src_1122 import task_func

# Mocking the requests.get function to simulate API responses
from unittest.mock import patch, MagicMock

@patch('requests.get')
def test_task_func(mock_get):
    # Mock response data
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "status": "success",
        "country": "United States",
        "regionName": "California",
        "city": "San Francisco",
        "lat": 37.7749,
        "lon": -122.4194,
        "timezone": "America/Los_Angeles"
    }
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Test input
    myString = "Check out this website: https://www.example.com and also visit http://another-example.org"
    API_KEY = "your_api_key_here"
    
    # Expected output
    expected_output = {
        "www.example.com": mock_response.json.return_value,
        "another-example.org": mock_response.json.return_value
    }
    
    # Run the function
    result = task_func(myString, API_KEY)
    
    # Assert the result
    assert result == expected_output

@patch('requests.get')
def test_task_func_no_urls(mock_get):
    # No URLs in the input string
    myString = "This is a test string without any URLs."
    API_KEY = "your_api_key_here"
    
    # Expected output
    expected_output = {}
    
    # Run the function
    result = task_func(myString, API_KEY)
    
    # Assert the result
    assert result == expected_output

@patch('requests.get')
def test_task_func_invalid_url(mock_get):
    # Invalid URL in the input string
    myString = "Check out this website: https://invalid-url"
    API_KEY = "your_api_key_here"
    
    # Mock response data for invalid URL
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "status": "fail",
        "message": "Invalid IP address"
    }
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Expected output
    expected_output = {
        "invalid-url": mock_response.json.return_value
    }
    
    # Run the function
    result = task_func(myString, API_KEY)
    
    # Assert the result
    assert result == expected_output