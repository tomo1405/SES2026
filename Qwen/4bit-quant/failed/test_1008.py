import pytest
from src_1008 import task_func
import requests
import pandas as pd
from unittest.mock import patch

# Mocking the requests.get method
@patch('src_1008.requests.get')
def test_task_func_success(mock_get):
    # Define a mock response
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Expected DataFrame
    expected_df = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': [30, 25]
    })
    
    # Call the function
    result_df = task_func('https://example.com/data')
    
    # Assert that the result is as expected
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('src_1008.requests.get')
def test_task_func_http_error(mock_get):
    # Define a mock response with a non-200 status code
    mock_response = requests.Response()
    mock_response.status_code = 404
    
    # Configure the mock to raise an HTTPError
    mock_get.return_value = mock_response
    mock_get.return_value.raise_for_status.side_effect = requests.HTTPError('HTTP Error 404: Not Found')
    
    # Assert that the function raises SystemError with the correct message
    with pytest.raises(SystemError, match="Network error occurred"):
        task_func('https://example.com/data')

@patch('src_1008.requests.get')
def test_task_func_invalid_json(mock_get):
    # Define a mock response with invalid JSON
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'not valid json'
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Assert that the function raises ValueError with the correct message
    with pytest.raises(ValueError, match="Invalid JSON format for DataFrame conversion"):
        task_func('https://example.com/data')

@patch('src_1008.requests.get')
def test_task_func_timeout(mock_get):
    # Configure the mock to raise a timeout error
    mock_get.side_effect = requests.Timeout('The request timed out')
    
    # Assert that the function raises SystemError with the correct message
    with pytest.raises(SystemError, match="Network error occurred"):
        task_func('https://example.com/data')