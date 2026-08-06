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
    # Test case 1: Test with valid data
    data = {'x': 1, 'y': 2, 'z': 3}
    json_file_name = 'data.json'
    expected_json_file_path = os.path.join(os.getcwd(), json_file_name)
    assert task_func(data, json_file_name) == expected_json_file_path

    # Test case 2: Test with empty data
    data = {}
    json_file_name = 'data.json'
    expected_json_file_path = os.path.join(os.getcwd(), json_file_name)
    assert task_func(data, json_file_name) == expected_json_file_path

    # Test case 3: Test with invalid data type
    data = 'invalid data type'
    json_file_name = 'data.json'
    with pytest.raises(TypeError):
        task_func(data, json_file_name)

    # Test case 4: Test with invalid file name
    data = {'x': 1, 'y': 2, 'z': 3}
    json_file_name = 'invalid_file_name.json'
    expected_json_file_path = os.path.join(os.getcwd(), json_file_name)
    assert task_func(data, json_file_name) == expected_json_file_path