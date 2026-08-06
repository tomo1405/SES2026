python
import json
import os
import pytest

def task_func(file_path):
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return False

    return isinstance(data, list) and all(isinstance(item, dict) for item in data)

def test_task_func():
    # Test case 1: Valid JSON file with list of dictionaries
    file_path = 'test_data.json'
    with open(file_path, 'w') as file:
        json.dump([{'a': 1}, {'b': 2}], file)
    assert task_func(file_path) == True

    # Test case 2: Invalid JSON file
    file_path = 'invalid_data.json'
    with open(file_path, 'w') as file:
        file.write('invalid json')
    assert task_func(file_path) == False

    # Test case 3: Non-existent file
    file_path = 'nonexistent_file.json'
    assert task_func(file_path) == False

    # Test case 4: Empty file
    file_path = 'empty_file.json'
    with open(file_path, 'w') as file:
        pass
    assert task_func(file_path) == False

    # Test case 5: Valid JSON file with non-list data
    file_path = 'non_list_data.json'
    with open(file_path, 'w') as file:
        json.dump({'a': 1}, file)
    assert task_func(file_path) == False

    # Test case 6: Valid JSON file with list of non-dictionary data
    file_path = 'non_dict_list_data.json'
    with open(file_path, 'w') as file:
        json.dump([{'a': 1}, ['b', 'c']], file)
    assert task_func(file_path) == False