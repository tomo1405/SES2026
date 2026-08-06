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
    # Test case 1
    data = {'a': 1, 'b': 2, 'c': 3}
    json_file_name = 'data1.json'
    expected_json_file_path = os.path.join(os.getcwd(), json_file_name)
    assert task_func(data, json_file_name) == expected_json_file_path

    # Test case 2
    data = {'a': 2, 'b': 3, 'c': 4}
    json_file_name = 'data2.json'
    expected_json_file_path = os.path.join(os.getcwd(), json_file_name)
    assert task_func(data, json_file_name) == expected_json_file_path

    # Test case 3
    data = {'a': 3, 'b': 4, 'c': 5}
    json_file_name = 'data3.json'
    expected_json_file_path = os.path.join(os.getcwd(), json_file_name)
    assert task_func(data, json_file_name) == expected_json_file_path