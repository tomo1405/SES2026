python
import json
import os
import glob
import pytest

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    files = glob.glob(os.path.join(directory, '*.json'))
    updated_files = 0

    for file in files:
        with open(file, 'r+') as f:
            data = json.load(f)
            if KEY not in data:
                data[KEY] = VALUE
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                updated_files += 1

    return updated_files

def test_task_func():
    # Test case 1: directory with no JSON files
    directory = 'tests/test_data/no_json_files'
    assert task_func(directory) == 0

    # Test case 2: directory with one JSON file
    directory = 'tests/test_data/one_json_file'
    assert task_func(directory) == 1

    # Test case 3: directory with multiple JSON files
    directory = 'tests/test_data/multiple_json_files'
    assert task_func(directory) == 2

    # Test case 4: directory with JSON file that already has the key-value pair
    directory = 'tests/test_data/json_file_with_key_value'
    assert task_func(directory) == 0

    # Test case 5: directory with JSON file that has invalid JSON format
    directory = 'tests/test_data/invalid_json_file'
    with pytest.raises(json.JSONDecodeError):
        task_func(directory)