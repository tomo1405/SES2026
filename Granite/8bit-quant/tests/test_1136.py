import collections
import json

import pytest
import requests
from src_1136 import task_func


def test_task_func():
    user = 'octocat'
    API_URL = 'https://api.github.com/users/'
    response = requests.get(API_URL + user + '/repos')
    data = json.loads(response.text)
    repos = {repo['name']: repo['created_at'] for repo in data}
    sorted_repos = collections.OrderedDict(sorted(repos.items(), key=lambda x: x[1]))
    expected_result = list(sorted_repos.keys())
    actual_result = task_func(user, API_URL)
    assert actual_result == expected_result

def test_task_func_with_default_api_url():
    user = 'octocat'
    response = requests.get('https://api.github.com/users/' + user + '/repos')
    data = json.loads(response.text)
    repos = {repo['name']: repo['created_at'] for repo in data}
    sorted_repos = collections.OrderedDict(sorted(repos.items(), key=lambda x: x[1]))
    expected_result = list(sorted_repos.keys())
    actual_result = task_func(user)
    assert actual_result == expected_result

def test_task_func_with_invalid_user():
    user = 'invalid_user'
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(user)