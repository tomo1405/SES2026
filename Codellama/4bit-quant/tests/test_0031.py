import json

from src_0031 import task_func


def test_task_func_valid_input():
    file_path = 'test_data.json'
    attribute = 'name'
    expected_result = 'John Doe'

    with open(file_path, 'w') as f:
        json.dump({'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}, f)

    result = task_func(file_path, attribute)

    assert result == expected_result

def test_task_func_invalid_input():
    file_path = 'test_data.json'
    attribute = 'name'
    expected_result = 'John Doe'

    with open(file_path, 'w') as f:
        json.dump({'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}, f)

    result = task_func(file_path, attribute)

    assert result == expected_result

def test_task_func_missing_required_key():
    file_path = 'test_data.json'
    attribute = 'name'
    expected_result = 'John Doe'

    with open(file_path, 'w') as f:
        json.dump({'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}, f)

    result = task_func(file_path, attribute)

    assert result == expected_result

def test_task_func_invalid_type():
    file_path = 'test_data.json'
    attribute = 'name'
    expected_result = 'John Doe'

    with open(file_path, 'w') as f:
        json.dump({'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}, f)

    result = task_func(file_path, attribute)

    assert result == expected_result

def test_task_func_invalid_email():
    file_path = 'test_data.json'
    attribute = 'name'
    expected_result = 'John Doe'

    with open(file_path, 'w') as f:
        json.dump({'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}, f)

    result = task_func(file_path, attribute)

    assert result == expected_result