import pytest
from src_0689 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    
    # Calculate expected output using StandardScaler
    scaler = StandardScaler()
    expected_output = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    # Get actual output from the function
    actual_output = task_func(df)
    
    # Check if the actual output matches the expected output
    pd.testing.assert_frame_equal(actual_output, expected_output)

def test_task_func_empty_df():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # The function should return an empty DataFrame
    expected_output = pd.DataFrame()
    actual_output = task_func(df)
    
    # Check if the actual output matches the expected output
    pd.testing.assert_frame_equal(actual_output, expected_output)

def test_task_func_single_row():
    # Create a DataFrame with a single row
    data = {
        'A': [1],
        'B': [5]
    }
    df = pd.DataFrame(data)
    
    # Calculate expected output using StandardScaler
    scaler = StandardScaler()
    expected_output = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    # Get actual output from the function
    actual_output = task_func(df)
    
    # Check if the actual output matches the expected output
    pd.testing.assert_frame_equal(actual_output, expected_output)