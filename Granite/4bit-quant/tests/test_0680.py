import pandas as pd
from collections import Counter
from src_0680 import task_func
import pytest

def test_task_func():
    # Create a sample DataFrame to test the function
    df = pd.DataFrame({'A': [1, 2, 2], 'B': [1, 2, 3]})
    
    # Call the function with the sample DataFrame
    result = task_func(df)
    
    # Define the expected result
    expected_result = {
        (1, 1): 1,
        (1, 2): 1,
        (2, 1): 1,
        (2, 2): 1,
        (2, 3): 1
    }
    
    # Assert that the result matches the expected result
    assert result == expected_result

def test_task_func_with_empty_df():
    # Create an empty DataFrame to test the function
    df = pd.DataFrame()
    
    # Call the function with the empty DataFrame
    result = task_func(df)
    
    # Define the expected result
    expected_result = {}
    
    # Assert that the result matches the expected result
    assert result == expected_result