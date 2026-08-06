python
import os
import json
from collections import Counter
import pytest

def task_func(json_files_path='./json_files/', key='name'):
    key_values = []

    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if key in data:
                    key_values.append(data[key])

    return dict(Counter(key_values))

def test_task_func():
    # Test case 1: Valid JSON files with unique values
    json_files_path = './json_files/'
    key = 'name'
    expected_result = {'John': 1, 'Jane': 1, 'Bob': 1}
    assert task_func(json_files_path, key) == expected_result

    # Test case 2: Valid JSON files with duplicate values
    json_files_path = './json_files_duplicate/'
    key = 'name'
    expected_result = {'John': 2, 'Jane': 2, 'Bob': 2}
    assert task_func(json_files_path, key) == expected_result

    # Test case 3: Invalid JSON files
    json_files_path = './json_files_invalid/'
    key = 'name'
    expected_result = {}
    assert task_func(json_files_path, key) == expected_result

    # Test case 4: JSON files with missing key
    json_files_path = './json_files_missing_key/'
    key = 'name'
    expected_result = {}
    assert task_func(json_files_path, key) == expected_result

    # Test case 5: JSON files with empty key
    json_files_path = './json_files_empty_key/'
    key = 'name'
    expected_result = {}
    assert task_func(json_files_path, key) == expected_result

    # Test case 6: JSON files with non-existent directory
    json_files_path = './non_existent_directory/'
    key = 'name'
    expected_result = {}
    assert task_func(json_files_path, key) == expected_result