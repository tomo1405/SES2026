import pytest
from src_0631 import task_func
import pandas as pd
import os

def test_task_func():
    # Create a sample DataFrame
    data = {'A': [1, 2, None], 'B': [None, 4, 5]}
    df = pd.DataFrame(data)
    
    # Define the filename and output directory
    filename = 'test_output.json'
    output_dir = './test_output'
    
    # Call the function
    result = task_func(df, filename, output_dir)
    
    # Check if the directory exists
    assert os.path.exists(output_dir)
    
    # Check if the file exists
    assert os.path.isfile(result)
    
    # Read the content of the file
    with open(result, 'r') as f:
        content = f.read()
    
    # Expected JSON content
    expected_content = '[{"A": 1, "B": null}, {"A": 2, "B": 4}, {"A": null, "B": 5}]'
    
    # Check if the content is as expected
    assert content == expected_content
    
    # Clean up: remove the created directory and file
    os.remove(result)
    os.rmdir(output_dir)