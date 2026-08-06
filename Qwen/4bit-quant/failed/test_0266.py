import pytest
from src_0266 import task_func
import os
import json

def test_task_func(tmpdir):
    # Prepare test data
    test_data = {'b': 2, 'c': 3}
    expected_data = {'b': 2, 'c': 3, 'a': 1}
    expected_freq = {'b': 1, 'c': 1, 'a': 1}

    # Create a temporary directory for the JSON file
    tmp_dir = tmpdir.mkdir("test_task_func")
    json_file_name = "test_data.json"
    json_file_path = task_func(test_data, json_file_name=json_file_name)

    # Check if the file exists
    assert os.path.exists(json_file_path)

    # Read the contents of the JSON file
    with open(json_file_path, 'r') as json_file:
        actual_data = json.load(json_file)

    # Verify the contents of the JSON file
    assert actual_data['data'] == expected_data
    assert actual_data['freq'] == expected_freq