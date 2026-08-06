import pytest
from src_0579 import task_func
import requests
from unittest.mock import patch

# Mocking the requests.get method
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f'HTTP Error {self.status_code}')

@patch('src_0579.requests.get')
def test_task_func_success(mock_get):
    # Prepare mock data
    mock_json_data = {
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
        "site_admin": False
    }
    mock_response = MockResponse(mock_json_data, 200)
    mock_get.return_value = mock_response

    # Call the function
    result = task_func("octocat")

    # Assertions
    assert result == mock_json_data

@patch('src_0579.requests.get')
def test_task_func_http_error(mock_get):
    # Prepare mock data
    mock_response = MockResponse({}, 404)
    mock_get.return_value = mock_response

    # Call the function and expect an exception
    with pytest.raises(Exception) as exc_info:
        task_func("nonexistentuser")

    # Assertions
    assert str(exc_info.value) == "Failed to fetch user data for 'nonexistentuser'. HTTP status: 404 - Not Found."

@patch('src_0579.requests.get')
def test_task_func_unicode_normalization(mock_get):
    # Prepare mock data with unicode characters
    mock_json_data = {
        "login": "octocat",
        "name": "José da Silva",
        "company": "GitHub Inc."
    }
    mock_response = MockResponse(mock_json_data, 200)
    mock_get.return_value = mock_response

    # Call the function
    result = task_func("octocat")

    # Assertions
    assert result["name"] == "Jose da Silva"
    assert result["company"] == "GitHub Inc."