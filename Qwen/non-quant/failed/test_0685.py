import pytest
from src_0685 import task_func
import pandas as pd
import numpy as np

def test_task_func_remove_column():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Call the function to remove column 'A'
    result = task_func(df, 'A')
    
    # Check if column 'A' is removed
    assert 'A' not in result.columns
    # Check if the remaining columns are correct
    assert list(result.columns) == ['B', 'IsEvenIndex']

def test_task_func_add_is_even_index_column():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Call the function
    result = task_func(df, 'A')
    
    # Check if 'IsEvenIndex' column is added
    assert 'IsEvenIndex' in result.columns
    # Check if the values in 'IsEvenIndex' are correct
    expected_is_even_index = [True, False, True]
    assert all(result['IsEvenIndex'] == expected_is_even_index)

def test_task_func_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Call the function with a non-existing column
    result = task_func(df, 'C')
    
    # Check if the DataFrame remains empty
    assert result.empty
    # Check if 'IsEvenIndex' column is added
    assert 'IsEvenIndex' in result.columns
    # Check if 'IsEvenIndex' column is empty
    assert result['IsEvenIndex'].empty

def test_task_func_single_row_dataframe():
    # Create a single row DataFrame
    data = {'A': [1]}
    df = pd.DataFrame(data)
    
    # Call the function to remove column 'A'
    result = task_func(df, 'A')
    
    # Check if column 'A' is removed
    assert 'A' not in result.columns
    # Check if the remaining columns are correct
    assert list(result.columns) == ['IsEvenIndex']
    # Check if the value in 'IsEvenIndex' is correct
    assert result['IsEvenIndex'][0] == True