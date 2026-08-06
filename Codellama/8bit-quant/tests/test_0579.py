import pytest
from src_0579 import task_func

def test_task_func_valid_username():
    username = 'octocat'
    expected_data = {
        'login': 'octocat',
        'id': 583231,
        'node_id': 'MDQ6VXNlcjU4MzIzMQ==',
        'avatar_url': 'https://avatars.githubusercontent.com/u/583231?v=4',
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
        'company': 'GitHub',
        'blog': 'https://github.blog',
        'location': 'San Francisco',
        'email': 'octocat@github.com',
        'hireable': False,
        'bio': 'There once was...',
        'twitter_username': 'octocat',
        'public_repos': 2,
        'public_gists': 1,
        'followers': 20,
        'following': 0,
        'created_at': '2008-01-14T04:33:35Z',
        'updated_at': '2008-01-14T04:33:35Z'
    }
    actual_data = task_func(username)
    assert actual_data == expected_data

def test_task_func_invalid_username():
    username = 'invalid_username'
    with pytest.raises(Exception) as e:
        task_func(username)
    assert str(e.value) == f"Failed to fetch user data for '{username}'. HTTP status: 404 - Not Found."