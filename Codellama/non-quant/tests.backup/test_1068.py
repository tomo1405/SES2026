import pytest
from src_1068 import task_func

def test_task_func_valid_repo_url():
    repo_url = "https://api.github.com/repos/python/cpython"
    repo_info = task_func(repo_url)
    assert repo_info["open_issues_count"] > 0

def test_task_func_invalid_repo_url():
    repo_url = "https://api.github.com/repos/python/invalid_repo"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(repo_url)

def test_task_func_api_rate_limit_exceeded():
    repo_url = "https://api.github.com/repos/python/cpython"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(repo_url)

def test_task_func_logging_warning():
    repo_url = "https://api.github.com/repos/python/cpython"
    with pytest.warns(UserWarning):
        task_func(repo_url)