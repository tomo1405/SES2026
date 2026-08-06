import pytest
from src_0725 import task_func
import os
import json
import tempfile

def test_task_func_valid_config():
    # Create a temporary JSON file with valid content
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write(json.dumps({"key": "value"}))
        temp_file_path = temp_file.name
    
    try:
        # Call the function with the path to the temporary file
        result = task_func(temp_file_path)
        
        # Assert that the result is the expected dictionary
        assert result == {"key": "value"}
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

def test_task_func_nonexistent_config():
    # Define a path to a non-existent file
    non_existent_path = "/path/to/nonexistent/file.json"
    
    # Assert that calling the function raises a FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(non_existent_path)
    
    # Assert that the error message is correct
    assert str(excinfo.value) == f"The configuration file {non_existent_path} does not exist."

def test_task_func_invalid_json():
    # Create a temporary file with invalid JSON content
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("invalid json")
        temp_file_path = temp_file.name
    
    try:
        # Assert that calling the function raises a json.JSONDecodeError
        with pytest.raises(json.JSONDecodeError):
            task_func(temp_file_path)
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)