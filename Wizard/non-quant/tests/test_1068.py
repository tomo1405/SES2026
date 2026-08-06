python
import requests
import logging
import pytest

from src_1068 import task_func

def test_task_func():
    # Test valid repo URL
    repo_url = "https://api.github.com/repos/octocat/Hello-World"
    response = requests.get(repo_url, timeout=2)
    response.raise_for_status()
    repo_info = response.json()
    assert task_func(repo_url) == repo_info

    # Test invalid repo URL
    with pytest.raises(requests.exceptions.RequestException):
        task_func("https://invalid.url")

    # Test API rate limit exceeded
    repo_url = "https://api.github.com/repos/octocat/Hello-World"
    response = requests.get(repo_url, timeout=2)
    response.status_code = 403
    response._content = b'{"message": "API rate limit exceeded"}'
    response.headers["Content-Type"] = "application/json"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(repo_url)

    # Test repo with more than 10000 open issues
    repo_url = "https://api.github.com/repos/octocat/Hello-World"
    response = requests.get(repo_url, timeout=2)
    response.status_code = 200
    response._content = b'{"open_issues_count": 10001}'
    response.headers["Content-Type"] = "application/json"
    with pytest.warns(UserWarning):
        task_func(repo_url)