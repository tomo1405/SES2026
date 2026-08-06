import pytest
from src_1068 import task_func
import requests

def test_task_func_success():
    # Mock a successful response
    mock_response = {
        "name": "test_repo",
        "open_issues_count": 5000,
    }
    with requests.get_mock("test_url", text=mock_response):
        result = task_func("test_url")
        assert result == mock_response

def test_task_func_api_rate_limit_exceeded():
    # Mock a rate limit exceeded response
    mock_response = {"message": "API rate limit exceeded"}
    with requests.get_mock("test_url", status_code=403, json=mock_response):
        with pytest.raises(requests.exceptions.HTTPError):
            task_func("test_url")

def test_task_func_request_exception():
    with requests.get_mock("test_url", exc=requests.RequestException):
        with pytest.raises(requests.exceptions.RequestException):
            task_func("test_url")