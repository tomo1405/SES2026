python
import pytest
import requests
import unicodedata

from src_0579 import task_func

def test_task_func():
    # Test case 1: Valid username
    response = requests.get('https://api.github.com/users/octocat')
    response.raise_for_status()
    user_data = response.json()
    expected_result = {
        'login': 'octocat',
        'id': 1538673,
        'node_id': 'MDQ6VXNlcjE1Mzg2NzM=',
        'avatar_url': 'https://avatars.githubusercontent.com/u/1538673?v=4',
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
        'site_admin': False,
        'name': 'The Octocat',
        'company': None,
        'blog': 'https://octodex.github.com/',
        'location': 'San Francisco',
        'email': None,
        'hireable': None,
        'bio': None,
        'twitter_username': 'octocat',
        'public_repos': 1,
        'public_gists': 0,
        'followers': 0,
        'following': 0,
        'created_at': '2008-05-16T17:57:11Z',
        'updated_at': '2021-03-29T17:53:35Z',
        'private_gists': 0,
        'total_private_repos': 0,
        'owned_private_repos': 0,
        'disk_usage': 10112,
        'collaborators': 0,
        'two_factor_authentication': True,
        'plan': {
            'name': 'Medium',
            'space': 400,
            'private_repos': 10,
            'collaborators': 0
        }
    }
    assert task_func('octocat') == expected_result

    # Test case 2: Invalid username
    with pytest.raises(Exception) as e:
        task_func('invalid_username')
    assert str(e.value) == "Failed to fetch user data for 'invalid_username'. HTTP status: 404 - Not Found."