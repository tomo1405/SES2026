import pytest
from src_0330 import task_func
import os
import json

def test_task_func_with_valid_json_file(tmpdir):
    # Create a temporary directory and a JSON file within it
    temp_dir = tmpdir.mkdir("temp")
    json_file = temp_dir.join("test.json")
    json_data = {
        "key1": "value1",
        "key2": "value2 (with parentheses)",
        "key3": "value3"
    }
    json_file.write(json.dumps(json_data))

    # Define the expected output
    expected_output = {
        "test.json": ['value1', 'value2', '(', ')', 'with', 'parentheses', 'value3']
    }

    # Call the function
    result = task_func(str(json_file))

    # Assert the result
    assert result == expected_output

def test_task_func_with_nonexistent_file():
    # Define a non-existent file path
    file_path = "non_existent_file.json"

    # Expect a FileNotFoundError to be raised
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

def test_task_func_with_empty_json_file(tmpdir):
    # Create a temporary directory and an empty JSON file within it
    temp_dir = tmpdir.mkdir("temp")
    json_file = temp_dir.join("empty.json")
    json_file.write("{}")

    # Define the expected output
    expected_output = {
        "empty.json": []
    }

    # Call the function
    result = task_func(str(json_file))

    # Assert the result
    assert result == expected_output

def test_task_func_with_custom_regex(tmpdir):
    # Create a temporary directory and a JSON file within it
    temp_dir = tmpdir.mkdir("temp")
    json_file = temp_dir.join("custom_regex.json")
    json_data = {
        "key1": "value1",
        "key2": "value2 (with parentheses)",
        "key3": "value3"
    }
    json_file.write(json.dumps(json_data))

    # Define a custom regex pattern
    regex_pattern = r'\d+'

    # Define the expected output
    expected_output = {
        "custom_regex.json": []
    }

    # Call the function with the custom regex pattern
    result = task_func(str(json_file), regex_pattern=regex_pattern)

    # Assert the result
    assert result == expected_output