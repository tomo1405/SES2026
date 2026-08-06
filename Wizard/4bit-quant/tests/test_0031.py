python
import json
import os
import re
import pytest

from src_0031 import task_func

def test_task_func():
    # Test case 1: Valid JSON file with all required fields and valid email
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example.com"
        }, f)
    assert task_func(file_path, 'name') == 'John Doe'

    # Test case 2: Valid JSON file with all required fields and invalid email
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({
            "name": "Jane Doe",
            "age": 25,
            "email": "jane.doe@example"
        }, f)
    with pytest.raises(ValueError) as e:
        task_func(file_path, 'name')
    assert str(e.value) == 'Email is not valid.'

    # Test case 3: Valid JSON file with missing required field
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({
            "name": "John Doe",
            "age": 30
        }, f)
    with pytest.raises(ValueError) as e:
        task_func(file_path, 'name')
    assert str(e.value) == "'email' is missing from the JSON object."

    # Test case 4: Valid JSON file with invalid field type
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({
            "name": "John Doe",
            "age": "30",
            "email": "john.doe@example.com"
        }, f)
    with pytest.raises(ValueError) as e:
        task_func(file_path, 'name')
    assert str(e.value) == "'age' is not of type <class 'int'>."

    # Test case 5: Invalid JSON file
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        f.write('Invalid JSON')
    with pytest.raises(ValueError) as e:
        task_func(file_path, 'name')
    assert str(e.value) == 'Expecting value: line 1 column 1 (char 0)'

    # Test case 6: Non-existent file
    file_path = 'non_existent_file.json'
    with pytest.raises(ValueError) as e:
        task_func(file_path, 'name')
    assert str(e.value) == 'non_existent_file.json does not exist.'