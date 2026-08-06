import pytest
from src_0680 import task_func
import pandas as pd
from collections import Counter

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 2, 3],
        'B': [4, 5, 5, 6]
    }
    df = pd.DataFrame(data)
    
    # Expected output
    expected_output = {
        (1, 4): 1,
        (2, 5): 2,
        (3, 6): 1
    }
    
    # Call the function
    result = task_func(df)
    
    # Assert the result
    assert result == expected_output

def test_task_func_empty_df():
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['A', 'B'])
    
    # Expected output
    expected_output = {}
    
    # Call the function
    result = task_func(df)
    
    # Assert the result
    assert result == expected_output

def test_task_func_single_row():
    # Create a DataFrame with a single row
    data = {
        'A': [1],
        'B': [2]
    }
    df = pd.DataFrame(data)
    
    # Expected output
    expected_output = {(1, 2): 1}
    
    # Call the function
    result = task_func(df)
    
    # Assert the result
    assert result == expected_output

def test_task_func_duplicate_rows():
    # Create a DataFrame with duplicate rows
    data = {
        'A': [1, 1, 1],
        'B': [2, 2, 2]
    }
    df = pd.DataFrame(data)
    
    # Expected output
    expected_output = {(1, 2): 3}
    
    # Call the function
    result = task_func(df)
    
    # Assert the result
    assert result == expected_output

def test_task_func_non_numeric_values():
    # Create a DataFrame with non-numeric values
    data = {
        'A': ['a', 'b', 'b'],
        'B': ['c', 'd', 'd']
    }
    df = pd.DataFrame(data)
    
    # Expected output
    expected_output = {('a', 'c'): 1, ('b', 'd'): 2}
    
    # Call the function
    result = task_func(df)
    
    # Assert the result
    assert result == expected_output