import pytest
from src_0031 import task_func
import os
import json

# Test cases for task_func

def test_task_func_valid_file():
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({"name": "John Doe", "age": 30, "email": "john.doe@example.com"}, f)
    result = task_func(file_path, 'name')
    assert result == "John Doe"
    os.remove(file_path)

def test_task_func_invalid_file():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.json', 'name')

def test_task_func_missing_key():
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({"name": "John Doe", "age": 30}, f)
    with pytest.raises(ValueError):
        task_func(file_path, 'age')
    os.remove(file_path)

def test_task_func_invalid_type():
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({"name": "John Doe", "age": "30", "email": "john.doe@example.com"}, f)
    with pytest.raises(ValueError):
        task_func(file_path, 'age')
    os.remove(file_path)

def test_task_func_invalid_email():
    file_path = 'test_data.json'
    with open(file_path, 'w') as f:
        json.dump({"name": "John Doe", "age": 30, "email": "invalid-email"}, f)
    with pytest.raises(ValueError):
        task_func(file_path, 'email')
    os.remove(file_path)