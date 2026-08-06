python
import collections
import json
import os
import pytest

def task_func(directory_path: str) -> dict:
    key_counts = collections.defaultdict(int)

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for key in data.keys():
                    key_counts[key] += 1

    return dict(key_counts)

def test_task_func():
    # Test case 1: directory with no JSON files
    directory_path = 'tests/test_data/no_json_files'
    expected_result = {}
    assert task_func(directory_path) == expected_result

    # Test case 2: directory with one JSON file with no keys
    directory_path = 'tests/test_data/one_json_file_no_keys'
    expected_result = {}
    assert task_func(directory_path) == expected_result

    # Test case 3: directory with one JSON file with one key
    directory_path = 'tests/test_data/one_json_file_one_key'
    expected_result = {'key1': 1}
    assert task_func(directory_path) == expected_result

    # Test case 4: directory with one JSON file with multiple keys
    directory_path = 'tests/test_data/one_json_file_multiple_keys'
    expected_result = {'key1': 1, 'key2': 2, 'key3': 1}
    assert task_func(directory_path) == expected_result

    # Test case 5: directory with multiple JSON files with multiple keys
    directory_path = 'tests/test_data/multiple_json_files_multiple_keys'
    expected_result = {'key1': 2, 'key2': 1, 'key3': 1, 'key4': 1}
    assert task_func(directory_path) == expected_result