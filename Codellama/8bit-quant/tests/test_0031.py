import json

import pytest
from src_0031 import task_func


def test_task_func_valid_input():
    file_path = 'test_data.json'
    attribute = 'name'
    expected_output = 'John Doe'

    with open(file_path, 'w') as f:
        json.dump({'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}, f)

    output = task_func(file_path, attribute)

    assert output == expected_output

def test_task_func_invalid_input():
    file_path = 'test_data.json'
    attribute = 'name'
    expected_output = 'John Doe'

    with open(file_path, 'w') as f:
        json.dump({'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}, f)

    with pytest.raises(ValueError):
        task_func(file_path, attribute)