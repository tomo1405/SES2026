python
import json
import requests
import pytest

def task_func(API_URL, endpoint, PREFIX):
    try:
        response = requests.get(API_URL + endpoint)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching data from API: {e}")

    filename = PREFIX + endpoint + '.json'
    with open(filename, 'w') as f:
        json.dump(data, f)

    return filename

def test_task_func():
    API_URL = 'https://jsonplaceholder.typicode.com/'
    endpoint = 'todos/1'
    PREFIX = 'todo_'

    filename = task_func(API_URL, endpoint, PREFIX)

    assert filename == 'todo_todos_1.json'
    assert os.path.isfile(filename)

    with open(filename, 'r') as f:
        data = json.load(f)

    assert data['userId'] == 1
    assert data['id'] == 1
    assert data['title'] == 'delectus aut autem'
    assert data['completed'] is False