python
import json
import urllib.request
import urllib.parse
import gzip
import pytest

def task_func(url_str, file_path):
    response = urllib.request.urlopen(url_str)
    data = response.read().decode()
    json_data = json.loads(data)

    with gzip.open(file_path, 'wb') as f_out:
        f_out.write(json.dumps(json_data).encode())

    return file_path

def test_task_func():
    url_str = 'https://jsonplaceholder.typicode.com/todos/1'
    file_path = 'test.json.gz'

    task_func(url_str, file_path)

    with gzip.open(file_path, 'rb') as f_in:
        data = f_in.read().decode()
        json_data = json.loads(data)

    assert json_data['userId'] == 1
    assert json_data['id'] == 1
    assert json_data['title'] == 'delectus aut autem'
    assert json_data['completed'] is False