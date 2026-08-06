import pytest
from src_1008 import task_func
import requests
import pandas as pd
from unittest.mock import patch

@patch('src_1008.requests.get')
def test_task_func_success(mock_get):
    # Mock successful response
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'
    mock_get.return_value = mock_response

    url = "http://example.com/data"
    df = task_func(url)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ['name', 'age']

@patch('src_1008.requests.get')
def test_task_func_http_error(mock_get):
    # Mock HTTP error response
    mock_response = requests.Response()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    url = "http://example.com/data"
    with pytest.raises(SystemError) as excinfo:
        task_func(url)

    assert "Network error occurred" in str(excinfo.value)

@patch('src_1008.requests.get')
def test_task_func_invalid_json(mock_get):
    # Mock invalid JSON response
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'invalid json'
    mock_get.return_value = mock_response

    url = "http://example.com/data"
    with pytest.raises(ValueError) as excinfo:
        task_func(url)

    assert "Invalid JSON format for DataFrame conversion" in str(excinfo.value)

@patch('src_1008.requests.get')
def test_task_func_timeout(mock_get):
    # Mock timeout error
    mock_get.side_effect = requests.exceptions.Timeout

    url = "http://example.com/data"
    with pytest.raises(SystemError) as excinfo:
        task_func(url)

    assert "Network error occurred" in str(excinfo.value)

@patch('src_1008.requests.get')
def test_task_func_connection_error(mock_get):
    # Mock connection error
    mock_get.side_effect = requests.exceptions.ConnectionError

    url = "http://example.com/data"
    with pytest.raises(SystemError) as excinfo:
        task_func(url)

    assert "Network error occurred" in str(excinfo.value)