python
import json
import os
import re
import pytest

def task_func(
    file_path,
    attribute,
    INPUT_JSON={
        "type": "object",
        "properties": {
            "name": {"type": str},
            "age": {"type": int},
            "email": {"type": str}
        },
        "required": ["name", "age", "email"]
    },
    EMAIL_REGEX=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"):
    if not os.path.isfile(file_path):
        raise ValueError(f'{file_path} does not exist.')

    with open(file_path, 'r') as f:
        data = json.load(f)

    for key in INPUT_JSON['required']:
        if key not in data:
            raise ValueError(f'{key} is missing from the JSON object.')
        if not isinstance(data[key], INPUT_JSON['properties'][key]['type']):
            raise ValueError(f'{key} is not of type {INPUT_JSON["properties"][key]["type"]}.')

    if 'email' in data and not re.fullmatch(EMAIL_REGEX, data['email']):
        raise ValueError('Email is not valid.')

    return data[attribute]

def test_task_func():
    # Test case 1: Valid JSON file with valid attribute
    with open('test_data.json', 'w') as f:
        json.dump({'name': 'John', 'age': 30, 'email': 'john@example.com'}, f)
    assert task_func('test_data.json', 'name') == 'John'

    # Test case 2: Valid JSON file with invalid attribute
    with open('test_data.json', 'w') as f:
        json.dump({'name': 'John', 'age': 30, 'email': 'john@example.com'}, f)
    with pytest.raises(KeyError):
        task_func('test_data.json', 'gender')

    # Test case 3: Invalid JSON file
    with open('test_data.json', 'w') as f:
        f.write('invalid JSON')
    with pytest.raises(json.JSONDecodeError):
        task_func('test_data.json', 'name')

    # Test case 4: JSON file with missing required attribute
    with open('test_data.json', 'w') as f:
        json.dump({'name': 'John', 'age': 30}, f)
    with pytest.raises(ValueError):
        task_func('test_data.json', 'email')

    # Test case 5: JSON file with invalid attribute type
    with open('test_data.json', 'w') as f:
        json.dump({'name': 'John', 'age': '30', 'email': 'john@example.com'}, f)
    with pytest.raises(ValueError):
        task_func('test_data.json', 'age')

    # Test case 6: JSON file with invalid email format
    with open('test_data.json', 'w') as f:
        json.dump({'name': 'John', 'age': 30, 'email': 'johnexamplecom'}, f)
    with pytest.raises(ValueError):
        task_func('test_data.json', 'email')

    # Test case 7: Non-existent file
    with pytest.raises(ValueError):
        task_func('non_existent_file.json', 'name')