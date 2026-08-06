python
import requests
import logging
import pytest

def task_func(repo_url: str) -> dict:
    try:
        response = requests.get(repo_url, timeout=2)
        response.raise_for_status()  # Raises HTTPError for bad requests
        repo_info = response.json()
        if (
            response.status_code == 403
            and repo_info.get("message") == "API rate limit exceeded"
        ):
            raise requests.exceptions.HTTPError("API rate limit exceeded")

        if repo_info.get("open_issues_count", 0) > 10000:
            logging.warning("The repository has more than 10000 open issues.")

        return repo_info

    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(
            f"Error fetching repo info: {e}"
        ) from e

def test_task_func():
    # Test case 1: Valid repo URL
    repo_url = "https://api.github.com/repos/octocat/Hello-World"
    expected_result = {
        "id": 1296269,
        "name": "Hello-World",
        "full_name": "octocat/Hello-World",
        "owner": {
            "login": "octocat",
            "id": 1,
            "node_id": "MDQ6VXNlcjE=",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/octocat",
            "html_url": "https://github.com/octocat",
            "followers_url": "https://api.github.com/users/octocat/followers",
            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "organizations_url": "https://api.github.com/users/octocat/orgs",
            "repos_url": "https://api.github.com/users/octocat/repos",
            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
            "received_events_url": "https://api.github.com/users/octocat/received_events",
            "type": "User",
            "site_admin": False,
        },
        "private": False,
        "html_url": "https://github.com/octocat/Hello-World",
        "description": "This your first repo!",
        "fork": False,
        "url": "https://api.github.com/repos/octocat/Hello-World",
        "created_at": "2011-01-26T19:01:12Z",
        "updated_at": "2011-01-26T19:14:43Z",
        "pushed_at": "2011-01-26T19:10:12Z",
        "homepage": "https://github.com",
        "size": 108,
        "stargazers_count": 80,
        "watchers_count": 80,
        "language": "Python",
        "forks_count": 9,
        "open_issues_count": 0,
        "master_branch": "master",
        "default_branch": "master",
        "score": 1.0,
    }
    result = task_func(repo_url)
    assert result == expected_result

    # Test case 2: Invalid repo URL
    repo_url = "https://api.github.com/repos/octocat/invalid_repo"
    with pytest.raises(requests.exceptions.RequestException):
        task_func(repo_url)

    # Test case 3: API rate limit exceeded
    repo_url = "https://api.github.com/repos/octocat/Hello-World"
    response = requests.Response()
    response.status_code = 403
    response._content = b'{"message": "API rate limit exceeded"}'
    response.headers = {"Content-Type": "application/json"}
    response.url = repo_url
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(repo_url)

    # Test case 4: More than 10000 open issues
    repo_url = "https://api.github.com/repos/octocat/Hello-World"
    response._content = b'{"open_issues_count": 10001}'
    with pytest.warns(UserWarning):
        task_func(repo_url)