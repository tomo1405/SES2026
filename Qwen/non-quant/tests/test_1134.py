import json
from unittest.mock import Mock, patch

import pytest
import requests
from src_1134 import task_func


@patch('requests.get')
def test_task_func_success(mock_get):
    # Arrange
    API_URL = "https://api.example.com"
    endpoint = "/data"
    PREFIX = "test_"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}
    mock_get.return_value = mock_response

    # Act
    result = task_func(API_URL, endpoint, PREFIX)

    # Assert
    assert result == "test_/data.json"
    mock_get.assert_called_once_with(API_URL + endpoint)
    with open(result, 'r') as f:
        data = json.load(f)
        assert data == {"key": "value"}

@patch('requests.get')
def test_task_func_failure(mock_get):
    # Arrange
    API_URL = "https://api.example.com"
    endpoint = "/data"
    PREFIX = "test_"
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    # Act & Assert
    with pytest.raises(RuntimeError) as excinfo:
        task_func(API_URL, endpoint, PREFIX)
    assert "Error fetching data from API" in str(excinfo.value)
    mock_get.assert_called_once_with(API_URL + endpoint)

@patch('requests.get')
def test_task_func_request_exception(mock_get):
    # Arrange
    API_URL = "https://api.example.com"
    endpoint = "/data"
    PREFIX = "test_"
    mock_get.side_effect = requests.RequestException("Network error")

    # Act & Assert
    with pytest.raises(RuntimeError) as excinfo:
        task_func(API_URL, endpoint, PREFIX)
    assert "Error fetching data from API: Network error" in str(excinfo.value)
    mock_get.assert_called_once_with(API_URL + endpoint)