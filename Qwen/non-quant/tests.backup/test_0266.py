import pytest
from src_0266 import task_func
import os
import json

def test_task_func_default_filename():
    # Prepare test data
    test_data = {'b': 2, 'c': 3}
    expected_data = {'b': 2, 'c': 3, 'a': 1}
    expected_freq = {'b': 1, 'c': 1, 'a': 1}

    # Call the function
    result_path = task_func(test_data)

    # Check if the file exists
    assert os.path.exists(result_path)

    # Read the content of the file
    with open(result_path, 'r') as json_file:
        content = json.load(json_file)

    # Check the content
    assert content['data'] == expected_data
    assert content['freq'] == expected_freq

    # Clean up
    os.remove(result_path)

def test_task_func_custom_filename():
    # Prepare test data
    test_data = {'x': 4, 'y': 5}
    expected_data = {'x': 4, 'y': 5, 'a': 1}
    expected_freq = {'x': 1, 'y': 1, 'a': 1}
    custom_filename = 'test_data.json'

    # Call the function
    result_path = task_func(test_data, custom_filename)

    # Check if the file exists
    assert os.path.exists(result_path)

    # Read the content of the file
    with open(result_path, 'r') as json_file:
        content = json.load(json_file)

    # Check the content
    assert content['data'] == expected_data
    assert content['freq'] == expected_freq

    # Clean up
    os.remove(result_path)

def test_task_func_existing_file():
    # Prepare test data
    test_data = {'z': 6}
    expected_data = {'z': 6, 'a': 1}
    expected_freq = {'z': 1, 'a': 1}
    filename = 'existing_data.json'

    # Create an existing file
    with open(filename, 'w') as json_file:
        json.dump({'data': {}, 'freq': {}}, json_file)

    # Call the function
    result_path = task_func(test_data, filename)

    # Check if the file exists
    assert os.path.exists(result_path)

    # Read the content of the file
    with open(result_path, 'r') as json_file:
        content = json.load(json_file)

    # Check the content
    assert content['data'] == expected_data
    assert content['freq'] == expected_freq

    # Clean up
    os.remove(result_path)