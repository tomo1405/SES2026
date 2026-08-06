import json
import os

from src_0266 import task_func


def test_task_func():
    # Test case 1: add new key 'a' with value 1
    data = {'b': 2, 'c': 3}
    json_file_name = 'data.json'
    json_file_path = task_func(data, json_file_name)
    assert json_file_path == os.path.join(os.getcwd(), json_file_name)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        assert json_data['data']['a'] == 1

    # Test case 2: calculate the frequency of values in `data`
    data = {'a': 1, 'b': 2, 'c': 3}
    json_file_name = 'data.json'
    json_file_path = task_func(data, json_file_name)
    assert json_file_path == os.path.join(os.getcwd(), json_file_name)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        assert json_data['freq'] == {'a': 1, 'b': 1, 'c': 1}

    # Test case 3: save the updated `data` and the `freq` into a JSON file
    data = {'a': 1, 'b': 2, 'c': 3}
    json_file_name = 'data.json'
    json_file_path = task_func(data, json_file_name)
    assert json_file_path == os.path.join(os.getcwd(), json_file_name)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        assert json_data['data'] == data
        assert json_data['freq'] == {'a': 1, 'b': 1, 'c': 1}