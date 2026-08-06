import pytest
from src_0579 import task_func
import requests
from unittest.mock import patch

def test_task_func_success():
    username = 'octocat'
    mock_response = {
        'login': 'octocat',
        'id': 1,
        'node_id': 'MDQ6VXNlcjE=',
        'avatar_url': 'https://github.com/images/error/octocat_happy.gif',
        'gravatar_id': '',
        'url': 'https://api.github.com/users/octocat',
        'html_url': 'https://github.com/octocat',
        'followers_url': 'https://api.github.com/users/octocat/followers',
        'following_url': 'https://api.github.com/users/octocat/following{/other_user}',
        'gists_url': 'https://api.github.com/users/octocat/gists{/gist_id}',
        'starred_url': 'https://api.github.com/users/octocat/starred{/owner}{/repo}',
        'subscriptions_url': 'https://api.github.com/users/octocat/subscriptions',
        'organizations_url': 'https://api.github.com/users/octocat/orgs',
        'repos_url': 'https://api.github.com/users/octocat/repos',
        'events_url': 'https://api.github.com/users/octocat/events{/privacy}',
        'received_events_url': 'https://api.github.com/users/octocat/received_events',
        'type': 'User',
        'site_admin': False
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        result = task_func(username)

    assert result == mock_response

def test_task_func_http_error():
    username = 'nonexistentuser'

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(
            response=mock_get.return_value
        )

        with pytest.raises(Exception) as excinfo:
            task_func(username)

    assert str(excinfo.value) == "Failed to fetch user data for 'nonexistentuser'. HTTP status: 404 - Not Found."

def test_task_func_unicode_normalization():
    username = 'octocat'
    mock_response = {
        'name': 'José da Silva',
        'bio': 'Python Developer 🐍'
    }

    expected_normalized_response = {
        'name': 'Jose da Silva',
        'bio': 'Python Developer '
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        result = task_func(username)

    assert result == expected_normalized_response