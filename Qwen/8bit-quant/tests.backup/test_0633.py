import pytest
from src_0633 import task_func
import pandas as pd
import os
import json

def test_task_func():
    # Create a sample DataFrame
    data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
    df = pd.DataFrame(data)
    
    # Define a filename
    filename = 'test_output.jsonl'
    
    # Call the function
    result = task_func(df, filename)
    
    # Check if the file path is correct
    expected_path = os.path.abspath(os.path.join('./output', filename))
    assert result == expected_path
    
    # Check if the file exists
    assert os.path.exists(expected_path)
    
    # Read the content of the file and check its contents
    with open(expected_path, 'r') as file:
        lines = file.readlines()
        records = [json.loads(line) for line in lines]
    
    # Check if the records match the original DataFrame
    expected_records = df.to_dict(orient='records')
    assert records == expected_records
    
    # Clean up the created file and directory
    os.remove(expected_path)
    os.rmdir('./output')

def test_task_func_empty_df():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Define a filename
    filename = 'empty_output.jsonl'
    
    # Call the function
    result = task_func(df, filename)
    
    # Check if the file path is correct
    expected_path = os.path.abspath(os.path.join('./output', filename))
    assert result == expected_path
    
    # Check if the file exists
    assert os.path.exists(expected_path)
    
    # Read the content of the file and check its contents
    with open(expected_path, 'r') as file:
        lines = file.readlines()
    
    # Check if the file is empty
    assert len(lines) == 0
    
    # Clean up the created file and directory
    os.remove(expected_path)
    os.rmdir('./output')