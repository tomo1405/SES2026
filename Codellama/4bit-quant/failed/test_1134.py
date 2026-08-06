import pytest
from src_1134 import task_func

def test_task_func():
    API_URL = 'https://api.example.com'
    endpoint = '/users'
    PREFIX = 'data_'

    filename = task_func(API_URL, endpoint, PREFIX)

    assert filename == 'data_users.json'

    with open(filename, 'r') as f:
        data = json.load(f)

    assert data == {'users': [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]}