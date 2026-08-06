python
import collections
import json
import requests

def task_func(user, API_URL='https://api.github.com/users/'):
    response = requests.get(API_URL + user + '/repos')
    data = json.loads(response.text)
    repos = {repo['name']: repo['created_at'] for repo in data}
    sorted_repos = collections.OrderedDict(sorted(repos.items(), key=lambda x: x[1]))
    return list(sorted_repos.keys())

def test_task_func():
    assert task_func('octocat') == ['Hello-World', 'octocat.github.io', 'Spoon-Knife', 'first-contributions']
    assert task_func('python') == ['cpython', 'peps', 'Python']
    assert task_func('google') == ['android-guidelines', 'android-ndk', 'android-platform', 'android-sdk', 'google-api-java-client', 'google-auth-library-java', 'google-cloud-java', 'google-http-java-client', 'google-oauth-java-client', 'google-play-services', 'google-test-api', 'google-truth']