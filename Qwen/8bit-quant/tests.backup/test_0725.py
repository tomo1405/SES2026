import pytest
from src_0725 import task_func
import os
import json
from tempfile import NamedTemporaryFile

def test_task_func_valid_file():
    # Create a temporary JSON file with some content
    with NamedTemporaryFile(delete=False, mode='w') as temp_file:
        json.dump({"key": "value"}, temp_file)
    
    try:
        result = task_func(temp_file.name)
        assert result == {"key": "value"}
    finally:
        os.remove(temp_file.name)

def test_task_func_nonexistent_file():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("nonexistent_file.json")
    assert "The configuration file nonexistent_file.json does not exist." in str(excinfo.value)

def test_task_func_empty_file():
    # Create a temporary empty file
    with NamedTemporaryFile(delete=False, mode='w') as temp_file:
        pass
    
    try:
        with pytest.raises(json.JSONDecodeError):
            task_func(temp_file.name)
    finally:
        os.remove(temp_file.name)

def test_task_func_invalid_json():
    # Create a temporary file with invalid JSON content
    with NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("{invalid json")
    
    try:
        with pytest.raises(json.JSONDecodeError):
            task_func(temp_file.name)
    finally:
        os.remove(temp_file.name)