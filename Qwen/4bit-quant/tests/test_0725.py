import json

import pytest
from src_0725 import task_func


def test_task_func_valid_file(tmpdir):
    # Create a temporary JSON file
    temp_file = tmpdir.join("config.json")
    temp_file.write(json.dumps({"key": "value"}))
    
    # Test the function with the valid file path
    result = task_func(str(temp_file))
    assert result == {"key": "value"}

def test_task_func_non_existent_file():
    # Test the function with a non-existent file path
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_config.json")
    assert str(excinfo.value) == "The configuration file non_existent_config.json does not exist."

def test_task_func_invalid_json(tmpdir):
    # Create a temporary file with invalid JSON content
    temp_file = tmpdir.join("config.json")
    temp_file.write("{invalid json}")
    
    # Test the function with the invalid JSON file
    with pytest.raises(json.JSONDecodeError):
        task_func(str(temp_file))