import collections
import json

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
    assert task_func(user, API_URL) == expected_result