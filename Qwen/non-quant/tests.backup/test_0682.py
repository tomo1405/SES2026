import pytest
from src_0682 import task_func
import pandas as pd
import json
import os

# Helper function to create a temporary JSON file
def create_temp_json_file(data):
    temp_file = "temp_test_file.json"
    with open(temp_file, 'w') as file:
        json.dump(data, file)
    return temp_file

# Helper function to clean up the temporary JSON file
def cleanup_temp_json_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def test_task_func():
    # Test data
    test_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"}
    ]
    
    # Create a temporary JSON file
    temp_file = create_temp_json_file(test_data)
    
    try:
        # Call the function
        result_df = task_func(temp_file, "age")
        
        # Expected output
        expected_output = pd.DataFrame([
            {"name": "Alice", "city": "New York"},
            {"name": "Bob", "city": "Los Angeles"}
        ])
        
        # Check if the returned DataFrame is correct
        pd.testing.assert_frame_equal(result_df, expected_output)
        
        # Read the modified JSON file and check its content
        with open(temp_file, 'r') as file:
            modified_data = json.load(file)
        
        expected_modified_data = [
            {"name": "Alice", "city": "New York"},
            {"name": "Bob", "city": "Los Angeles"}
        ]
        
        assert modified_data == expected_modified_data
    
    finally:
        # Clean up the temporary file
        cleanup_temp_json_file(temp_file)