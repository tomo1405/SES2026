python
import pytest
import requests
import logging

from src_1068 import task_func

def test_task_func():
    # Test case 1: Valid repo URL
    response = requests.get("https://api.github.com/repos/octocat/Hello-World")
    response.raise_for_status()
    repo_info = response.json()
    assert task_func("https://api.github.com/repos/octocat/Hello-World") == repo_info

    # Test case 2: Invalid repo URL
    with pytest.raises(requests.exceptions.RequestException):
        task_func("https://api.github.com/repos/octocat/invalid_repo")

    # Test case 3: API rate limit exceeded
    response = requests.get("https://api.github.com/rate_limit")
    response.raise_for_status()
    rate_limit_info = response.json()
    if rate_limit_info["resources"]["core"]["remaining"] == 0:
        response = requests.get("https://api.github.com/repos/octocat/Hello-World")
        response.raise_for_status()
        repo_info = response.json()
        if (
            response.status_code == 403
            and repo_info.get("message") == "API rate limit exceeded"
        ):
            with pytest.raises(requests.exceptions.HTTPError):
                task_func("https://api.github.com/repos/octocat/Hello-World")
        else:
            assert task_func("https://api.github.com/repos/octocat/Hello-World") == repo_info
    else:
        assert task_func("https://api.github.com/repos/octocat/Hello-World") == repo_info

    # Test case 4: More than 10000 open issues
    response = requests.get("https://api.github.com/repos/octocat/Hello-World")
    response.raise_for_status()
    repo_info = response.json()
    if repo_info.get("open_issues_count", 0) > 10000:
        with pytest.warns(UserWarning):
            task_func("https://api.github.com/repos/octocat/Hello-World")
    else:
        assert task_func("https://api.github.com/repos/octocat/Hello-World") == repo_info