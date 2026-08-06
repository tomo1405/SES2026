import pytest
from src_1136 import task_func

def test_task_func():
    user = 'example_user'
    API_URL = 'https://api.github.com/users/'
    response = requests.get(API_URL + user + '/repos')
    data = json.loads(response.text)
    repos = {repo['name']: repo['created_at'] for repo in data}
    sorted_repos = collections.OrderedDict(sorted(repos.items(), key=lambda x: x[1]))
    expected_result = list(sorted_repos.keys())
    actual_result = task_func(user, API_URL)
    assert actual_result == expected_result