import json
import os

import pytest
from src_0031 import task_func


# Mocking os.path.isfile to simulate file existence
def mock_isfile(file_path):
    return file_path == "existing_file.json"

# Mocking json.load to simulate JSON content
def mock_json_load(file):
    return {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }

# Monkey patching os.path.isfile and json.load
@pytest.fixture(autouse=True)
def patch_os_and_json(monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)
    monkeypatch.setattr(json, 'load', mock_json_load)

def test_task_func_valid_input():
    result = task_func("existing_file.json", "name")
    assert result == "John Doe"

def test_task_func_missing_file():
    with pytest.raises(ValueError, match="non_existent_file.json does not exist."):
        task_func("non_existent_file.json", "name")

def test_task_func_missing_required_attribute():
    def mock_json_load_missing_name(file):
        return {
            "age": 30,
            "email": "john.doe@example.com"
        }
    monkeypatch.setattr(json, 'load', mock_json_load_missing_name)
    with pytest.raises(ValueError, match="name is missing from the JSON object."):
        task_func("existing_file.json", "name")

def test_task_func_invalid_type():
    def mock_json_load_invalid_age(file):
        return {
            "name": "John Doe",
            "age": "thirty",
            "email": "john.doe@example.com"
        }
    monkeypatch.setattr(json, 'load', mock_json_load_invalid_age)
    with pytest.raises(ValueError, match="age is not of type <class 'int'>."):
        task_func("existing_file.json", "age")

def test_task_func_invalid_email():
    def mock_json_load_invalid_email(file):
        return {
            "name": "John Doe",
            "age": 30,
            "email": "invalid-email"
        }
    monkeypatch.setattr(json, 'load', mock_json_load_invalid_email)
    with pytest.raises(ValueError, match="Email is not valid."):
        task_func("existing_file.json", "email")

def test_task_func_nonexistent_attribute():
    with pytest.raises(KeyError):
        task_func("existing_file.json", "address")