python
import collections
import json
import os
import pytest

def task_func(data, json_file_name='data.json'):
    # Add new key 'a' with value 1
    data['a'] = 1

    # Calculate the frequency of values in `data`
    freq = collections.Counter(data.values())

    # Save the updated `data` and the `freq` into a JSON file
    json_data = {'data': data, 'freq': dict(freq)}
    json_file_path = os.path.join(os.getcwd(), json_file_name)
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)

    return json_file_path

def test_task_func():
    data = {'a': 1, 'b': 2, 'c': 3}
    json_file_path = task_func(data)
    assert os.path.isfile(json_file_path)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        assert json_data['data'] == {'a': 1, 'b': 2, 'c': 3}
        assert json_data['freq'] == {'1': 1, '2': 1, '3': 1}
    os.remove(json_file_path)

if __name__ == '__main__':
    test_task_func()