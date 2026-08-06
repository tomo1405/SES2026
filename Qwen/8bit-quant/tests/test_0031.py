import json
import os

import pytest
from src_0031 import task_func


# Mocking os.path.isfile to simulate file existence
class MockPath:
    @staticmethod
    def isfile(file_path):
        return file_path == "existing_file.json"

# Mocking json.load to simulate reading JSON data
class MockJson:
    @staticmethod
    def load(f):
        return {
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example.com"
        }

# Patching os.path.isfile and json.load
@pytest.fixture(autouse=True)
def patch_os_path_isfile(monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', MockPath.isfile)

@pytest.fixture(autouse=True)
def patch_json_load(monkeypatch):
    monkeypatch.setattr(json, 'load', MockJson.load)

def test_task_func_valid_file_and_data():
    result = task_func("existing_file.json", "name")
    assert result == "John Doe"

def test_task_func_missing_required_attribute():
    with pytest.raises(ValueError, match="age is missing from the JSON object."):
        task_func("existing_file.json", "age")

def test_task_func_invalid_type_for_required_attribute():
    mock_json = {
        "name": "John Doe",
        "age": "thirty",
        "email": "john.doe@example.com"
    }
    with pytest.raises(ValueError, match="age is not of type <class 'int'>."):
        task_func("existing_file.json", "age", INPUT_JSON={
            "type": "object",
            "properties": {
                "name": {"type": str},  
                "age": {"type": int},   
                "email": {"type": str}  
            },
            "required": ["name", "age", "email"]
        })

def test_task_func_invalid_email():
    mock_json = {
        "name": "John Doe",
        "age": 30,
        "email": "invalid-email"
    }
    with pytest.raises(ValueError, match="Email is not valid."):
        task_func("existing_file.json", "email", INPUT_JSON={
            "type": "object",
            "properties": {
                "name": {"type": str},  
                "age": {"type": int},   
                "email": {"type": str}  
            },
            "required": ["name", "age", "email"]
        })

def test_task_func_nonexistent_file():
    with pytest.raises(ValueError, match="nonexistent_file.json does not exist."):
        task_func("nonexistent_file.json", "name")