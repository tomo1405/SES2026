import pytest
from src_0579 import task_func

def test_task_func():
    username = 'example_user'
    expected_result = {
        'login': 'example_user',
        'id': 1234567890,
        'node_id': 'ABCDEF1234567890',
        'avatar_url': 'https://example.com/avatar.png',
        'gravatar_id': '',
        'url': 'https://api.github.com/users/example_user',
        'html_url': 'https://github.com/example_user',
        'followers_url': 'https://api.github.com/users/example_user/followers',
        'following_url': 'https://api.github.com/users/example_user/following{/other_user}',
        'gists_url': 'https://api.github.com/users/example_user/gists{/gist_id}',
        'starred_url': 'https://api.github.com/users/example_user/starred{/owner}{/repo}',
        'subscriptions_url': 'https://api.github.com/users/example_user/subscriptions',
        'organizations_url': 'https://api.github.com/users/example_user/orgs',
        'repos_url': 'https://api.github.com/users/example_user/repos',
        'events_url': 'https://api.github.com/users/example_user/events{/privacy}',
        'received_events_url': 'https://api.github.com/users/example_user/received_events',
        'type': 'User',
        'site_admin': False
    }

    result = task_func(username)

    assert result == expected_result