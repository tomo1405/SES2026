python
import collections
import json
import requests
import pytest

def task_func(user, API_URL='https://api.github.com/users/'):
    response = requests.get(API_URL + user + '/repos')
    data = json.loads(response.text)
    repos = {repo['name']: repo['created_at'] for repo in data}
    sorted_repos = collections.OrderedDict(sorted(repos.items(), key=lambda x: x[1]))
    return list(sorted_repos.keys())

def test_task_func():
    # Test case 1
    user = 'octocat'
    expected_result = ['Hello-World', 'Hello-World2', 'Hello-World3']
    result = task_func(user)
    assert result == expected_result
    
    # Test case 2
    user = 'not_a_user'
    expected_result = []
    result = task_func(user)
    assert result == expected_result
    
    # Test case 3
    user = 'octocat'
    API_URL = 'https://api.github.com/not_a_url/'
    expected_result = []
    result = task_func(user, API_URL)
    assert result == expected_result