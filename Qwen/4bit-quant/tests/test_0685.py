import pytest
from src_0685 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Specify the column to drop
    col_to_drop = 'A'
    
    # Expected result after dropping column 'A' and adding 'IsEvenIndex'
    expected_data = {'B': [4, 5, 6], 'IsEvenIndex': [True, False, True]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, col_to_drop)
    
    # Check if the result matches the expected DataFrame
    assert result_df.equals(expected_df), "The result does not match the expected output."

def test_task_func_with_empty_df():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Specify the column to drop (doesn't matter since the DF is empty)
    col_to_drop = 'A'
    
    # Expected result after dropping column 'A' and adding 'IsEvenIndex'
    expected_data = {'IsEvenIndex': []}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, col_to_drop)
    
    # Check if the result matches the expected DataFrame
    assert result_df.equals(expected_df), "The result does not match the expected output."

def test_task_func_with_nonexistent_column():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Specify a non-existent column to drop
    col_to_drop = 'C'
    
    # Expected result after trying to drop non-existent column 'C' and adding 'IsEvenIndex'
    expected_data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'IsEvenIndex': [True, False, True]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, col_to_drop)
    
    # Check if the result matches the expected DataFrame
    assert result_df.equals(expected_df), "The result does not match the expected output."