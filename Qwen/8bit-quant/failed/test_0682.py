import pytest
from src_0682 import task_func
import pandas as pd
import json
import os

# Helper function to create a temporary JSON file
def create_temp_json_file(data):
    temp_file = 'temp.json'
    with open(temp_file, 'w') as file:
        json.dump(data, file)
    return temp_file

# Helper function to read JSON file content
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Test cases
def test_task_func():
    # Create a temporary JSON file with sample data
    data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25}
    ]
    temp_file = create_temp_json_file(data)

    # Call the function to be tested
    result_df = task_func(temp_file, 'age')

    # Check if the DataFrame is correct after dropping the 'age' column
    expected_df = pd.DataFrame({
        "id": [1, 2],
        "name": ["Alice", "Bob"]
    })
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Check if the JSON file has been updated correctly
    updated_data = read_json_file(temp_file)
    assert updated_data == [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

    # Clean up the temporary file
    os.remove(temp_file)

def test_task_func_key_not_exists():
    # Create a temporary JSON file with sample data
    data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25}
    ]
    temp_file = create_temp_json_file(data)

    # Call the function to be tested with a non-existing key
    with pytest.raises(KeyError):
        task_func(temp_file, 'gender')

    # Clean up the temporary file
    os.remove(temp_file)

def test_task_func_empty_file():
    # Create a temporary empty JSON file
    temp_file = create_temp_json_file([])

    # Call the function to be tested
    result_df = task_func(temp_file, 'age')

    # Check if the DataFrame is empty
    expected_df = pd.DataFrame(columns=['id', 'name'])
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Check if the JSON file has been updated correctly (remains empty)
    updated_data = read_json_file(temp_file)
    assert updated_data == []

    # Clean up the temporary file
    os.remove(temp_file)