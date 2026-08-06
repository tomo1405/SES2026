import json

from src_0207 import task_func


def test_task_func():
    file_name = 'test_data.csv'
    json_file_name = task_func(file_name)
    assert json_file_name == 'test_data.json'

    with open(json_file_name, 'r') as f:
        data = json.load(f)
        assert data == [{'name': 'John', 'age': '25'}, {'name': 'Jane', 'age': '30'}]