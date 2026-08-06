import pytest
from src_1068 import task_func
import requests
import logging
from unittest.mock import patch, MagicMock

# Mocking the requests.get function to simulate API responses
@patch('requests.get')
def test_task_func_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "open_issues_count": 5000,
        "name": "test-repo",
        "owner": {"login": "test-user"}
    }
    mock_get.return_value = mock_response

    result = task_func("https://api.github.com/repos/test-user/test-repo")
    assert result == {
        "open_issues_count": 5000,
        "name": "test-repo",
        "owner": {"login": "test-user"}
    }

@patch('requests.get')
def test_task_func_api_rate_limit_exceeded(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 403
    mock_response.json.return_value = {
        "message": "API rate limit exceeded"
    }
    mock_get.return_value = mock_response

    with pytest.raises(requests.exceptions.HTTPError, match="API rate limit exceeded"):
        task_func("https://api.github.com/repos/test-user/test-repo")

@patch('requests.get')
def test_task_func_http_error(mock_get):
    mock_get.side_effect = requests.exceptions.HTTPError("HTTP error occurred")

    with pytest.raises(requests.exceptions.RequestException, match="Error fetching repo info: HTTP error occurred"):
        task_func("https://api.github.com/repos/test-user/test-repo")

@patch('requests.get')
def test_task_func_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Connection error occurred")

    with pytest.raises(requests.exceptions.RequestException, match="Error fetching repo info: Connection error occurred"):
        task_func("https://api.github.com/repos/test-user/test-repo")

@patch('requests.get')
def test_task_func_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

    with pytest.raises(requests.exceptions.RequestException, match="Error fetching repo info: Request timed out"):
        task_func("https://api.github.com/repos/test-user/test-repo")

@patch('requests.get')
def test_task_func_too_many_issues(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "open_issues_count": 15000,
        "name": "test-repo",
        "owner": {"login": "test-user"}
    }
    mock_get.return_value = mock_response

    with patch.object(logging, 'warning') as mock_warning:
        task_func("https://api.github.com/repos/test-user/test-repo")
        mock_warning.assert_called_once_with("The repository has more than 10000 open issues.")