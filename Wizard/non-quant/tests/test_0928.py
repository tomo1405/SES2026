python
import pandas as pd
import pytest
from src_0928 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    file_path = 'data.csv'
    column_name = 'column_name'
    expected_output = pd.DataFrame({'column_name': [0, 1, 2]})
    actual_output = task_func(file_path, column_name)
    assert actual_output.equals(expected_output)
    
    # Test case 2: Test with invalid input (empty file_path)
    file_path = ''
    column_name = 'column_name'
    expected_output = pd.DataFrame({'column_name': []})
    actual_output = task_func(file_path, column_name)
    assert actual_output.equals(expected_output)
    
    # Test case 3: Test with invalid input (empty column_name)
    file_path = 'data.csv'
    column_name = ''
    expected_output = pd.DataFrame({'column_name': []})
    actual_output = task_func(file_path, column_name)
    assert actual_output.equals(expected_output)
    
    # Test case 4: Test with invalid input (non-existent file_path)
    file_path = 'nonexistent.csv'
    column_name = 'column_name'
    expected_output = pd.DataFrame({'column_name': []})
    actual_output = task_func(file_path, column_name)
    assert actual_output.equals(expected_output)