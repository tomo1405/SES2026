import pytest
from src_0061 import task_func
import pandas as pd
import json
import os

def test_task_func():
    # Test data
    result = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
    
    # Define temporary file paths
    csv_file_path = "test_output.csv"
    json_file_path = "test_output.json"
    
    # Call the function
    task_func(result, csv_file_path, json_file_path)
    
    # Check CSV output
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(result))
    
    # Check JSON output
    with open(json_file_path, 'r') as f:
        loaded_data = json.load(f)
    assert loaded_data == result
    
    # Clean up files
    os.remove(csv_file_path)
    os.remove(json_file_path)