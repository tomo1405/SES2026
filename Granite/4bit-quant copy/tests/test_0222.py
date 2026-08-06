import pytest
import numpy as np
from scipy import stats
from src_0222 import task_func

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

# Test case 1: Valid input
def test_valid_input():
    # Create sample input
    df = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'feature3': [10, 20, 30, 40, 50],
        'feature4': [50, 40, 30, 20, 10],
        'feature5': [100, 200, 300, 400, 500]
    })
    dct = {'feature1': 1, 'feature2': 2, 'feature3': 3, 'feature4': 4, 'feature5': 5}
    
    # Call the function
    result = task_func(df, dct)
    
    # Check if the result is a dictionary
    assert isinstance(result, dict)
    
    # Check if the keys of the dictionary match the features
    assert set(result.keys()) == set(FEATURES)
    
    # Check if the values of the dictionary are dictionaries
    for feature, stats in result.items():
        assert isinstance(stats, dict)
        
        # Check if the keys of the nested dictionary match the expected statistics
        assert set(stats.keys()) == set(['mean', 'median', 'mode', 'variance'])
        
        # Check if the values of the nested dictionary are of the correct type
        assert isinstance(stats['mean'], (int, float))
        assert isinstance(stats['median'], (int, float))
        assert isinstance(stats['mode'], int)
        assert isinstance(stats['variance'], (int, float))

# Test case 2: Invalid input
def test_invalid_input():
    # Create sample input
    df = 'invalid input'
    dct = 'invalid input'
    
    # Call the function
    result = task_func(df, dct)
    
    # Check if the result is a string
    assert isinstance(result, str)
    
    # Check if the result contains the expected error message
    assert "Invalid input" in result