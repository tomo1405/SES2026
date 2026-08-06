import pytest
from src_1068 import task_func
import requests
from unittest.mock import patch, MagicMock

def test_task_func_success():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "open_issues_count": 5000,
        "name": "test-repo",
        "owner": {"login": "test-user"}
    }
    
    with patch('requests.get', return_value=mock_response):
        result = task_func("https://api.github.com/repos/test-user/test-repo")
        assert result == {
            "open_issues_count": 5000,
            "name": "test-repo",
            "owner": {"login": "test-user"}
        }

def test_task_func_api_rate_limit_exceeded():
    mock_response = MagicMock()
    mock_response.status_code = 403
    mock_response.json.return_value = {
        "message": "API rate limit exceeded"
    }
    
    with patch('requests.get', return_value=mock_response):
        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            task_func("https://api.github.com/repos/test-user/test-repo")
        assert str(excinfo.value) == "API rate limit exceeded"

def test_task_func_open_issues_count_exceeds_10000():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "open_issues_count": 15000,
        "name": "test-repo",
        "owner": {"login": "test-user"}
    }
    
    with patch('requests.get', return_value=mock_response):
        with patch('logging.warning') as mock_warning:
            task_func("https://api.github.com/repos/test-user/test-repo")
            mock_warning.assert_called_once_with("The repository has more than 10000 open issues.")

def test_task_func_request_exception():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        with pytest.raises(requests.exceptions.RequestException) as excinfo:
            task_func("https://api.github.com/repos/test-user/test-repo")
        assert str(excinfo.value) == "Error fetching repo info: Network error"