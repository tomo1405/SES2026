import json
from unittest.mock import patch

import pytest
import requests
from src_1136 import task_func


@patch('src_1136.requests.get')
def test_task_func(mock_get):
    # Mock response
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'[{"name": "repo1", "created_at": "2020-01-01T00:00:00Z"}, {"name": "repo2", "created_at": "2019-01-01T00:00:00Z"}]'
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Call the function with a test user
    result = task_func('test_user')
    
    # Assert the result is as expected
    assert result == ['repo2', 'repo1']

@patch('src_1136.requests.get')
def test_task_func_no_repos(mock_get):
    # Mock response with no repositories
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'[]'
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Call the function with a test user
    result = task_func('test_user')
    
    # Assert the result is as expected
    assert result == []

@patch('src_1136.requests.get')
def test_task_func_api_error(mock_get):
    # Mock response with an error status code
    mock_response = requests.Response()
    mock_response.status_code = 404
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Call the function with a test user and expect an exception
    with pytest.raises(requests.exceptions.HTTPError):
        task_func('test_user')

@patch('src_1136.requests.get')
def test_task_func_invalid_json(mock_get):
    # Mock response with invalid JSON
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'invalid json'
    
    # Configure the mock to return the mock response
    mock_get.return_value = mock_response
    
    # Call the function with a test user and expect an exception
    with pytest.raises(json.JSONDecodeError):
        task_func('test_user')