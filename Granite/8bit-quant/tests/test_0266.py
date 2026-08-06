import json
import os

from src_0266 import task_func


def test_task_func():
    data = {'a': 1, 'b': 2, 'c': 1}
    json_file_name = 'test_data.json'
    json_file_path = task_func(data, json_file_name)

    # Assert that the JSON file was created
    assert os.path.exists(json_file_path)

    # Assert that the JSON file contains the expected data
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        assert json_data['data'] == data
        assert json_data['freq'] == {'1': 2, '2': 1}

    # Clean up the test JSON file
    os.remove(json_file_path)