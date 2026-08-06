import pytest
from src_0149 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'C', 'A', 'B']}
    df = pd.DataFrame(data)
    
    # Expected output after encoding
    expected_data = {'Category': [0, 1, 2, 0, 1]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'Category')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_df), "The function did not encode the column correctly."

def test_task_func_with_empty_column():
    # Create a sample DataFrame with an empty column
    data = {'Category': []}
    df = pd.DataFrame(data)
    
    # Expected output after encoding
    expected_data = {'Category': []}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'Category')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_df), "The function did not handle an empty column correctly."

def test_task_func_with_single_value_column():
    # Create a sample DataFrame with a single value column
    data = {'Category': ['A', 'A', 'A']}
    df = pd.DataFrame(data)
    
    # Expected output after encoding
    expected_data = {'Category': [0, 0, 0]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'Category')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_df), "The function did not handle a single value column correctly."