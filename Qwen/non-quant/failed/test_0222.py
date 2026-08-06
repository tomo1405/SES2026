import pytest
from src_0222 import task_func
import pandas as pd
import numpy as np
from scipy import stats

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'feature3': [2, 3, 4, 5, 6],
        'feature4': [6, 5, 4, 3, 2],
        'feature5': [3, 4, 5, 6, 7]
    }
    df = pd.DataFrame(data)
    
    # Create a sample dictionary for replacement
    dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    
    # Expected output
    expected_output = {
        'feature1': {'mean': 30.0, 'median': 30.0, 'mode': 30, 'variance': 800.0},
        'feature2': {'mean': 30.0, 'median': 30.0, 'mode': 30, 'variance': 800.0},
        'feature3': {'mean': 40.0, 'median': 40.0, 'mode': 40, 'variance': 800.0},
        'feature4': {'mean': 50.0, 'median': 50.0, 'mode': 50, 'variance': 800.0},
        'feature5': {'mean': 60.0, 'median': 60.0, 'mode': 60, 'variance': 800.0}
    }
    
    # Run the function
    result = task_func(df, dct)
    
    # Check if the result matches the expected output
    assert result == expected_output

def test_task_func_invalid_input():
    # Create a sample DataFrame with missing values
    data = {
        'feature1': [1, 2, None, 4, 5],
        'feature2': [5, None, 3, 2, 1],
        'feature3': [None, 3, 4, 5, 6],
        'feature4': [6, 5, 4, None, 2],
        'feature5': [3, 4, 5, 6, None]
    }
    df = pd.DataFrame(data)
    
    # Create a sample dictionary for replacement
    dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    
    # Run the function
    result = task_func(df, dct)
    
    # Check if the result is "Invalid input"
    assert result == "Invalid input"

def test_task_func_no_features():
    # Create a sample DataFrame with no features
    data = {}
    df = pd.DataFrame(data)
    
    # Create a sample dictionary for replacement
    dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    
    # Run the function
    result = task_func(df, dct)
    
    # Check if the result is "Invalid input"
    assert result == "Invalid input"

def test_task_func_empty_df():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Create a sample dictionary for replacement
    dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    
    # Run the function
    result = task_func(df, dct)
    
    # Check if the result is "Invalid input"
    assert result == "Invalid input"