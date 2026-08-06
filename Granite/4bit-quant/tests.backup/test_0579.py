import pytest
from src_0579 import task_func

def test_task_func():
    username = 'example_user'
    response = task_func(username)
    assert response['login'] == username
    assert response['id'] is not None
    assert response['node_id'] is not None
    assert response['avatar_url'] is not None
    assert response['gravatar_id'] is not None
    assert response['url'] is not None
    assert response['html_url'] is not None
    assert response['followers_url'] is not None
    assert response['following_url'] is not None
    assert response['gists_url'] is not None
    assert response['starred_url'] is not None
    assert response['subscriptions_url'] is not None
    assert response['organizations_url'] is not None
    assert response['repos_url'] is not None
    assert response['events_url'] is not None
    assert response['received_events_url'] is not None
    assert response['type'] is not None
    assert response['site_admin'] is not None

def test_task_func_with_invalid_username():
    username = 'invalid_user'
    with pytest.raises(Exception) as exc_info:
        task_func(username)
    assert 'Failed to fetch user data for' in str(exc_info.value)