import pytest
from src_0222 import task_func
import pandas as pd
import numpy as np
from scipy import stats

# Test data
@pytest.fixture
def sample_df():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'feature3': [2, 3, 4, 5, 6],
        'feature4': [6, 5, 4, 3, 2],
        'feature5': [3, 3, 3, 3, 3]
    }
    return pd.DataFrame(data)

@pytest.fixture
def replacement_dict():
    return {'feature1': {1: 10, 2: 20}, 'feature2': {5: 50, 4: 40}}

def test_task_func(sample_df, replacement_dict):
    expected_output = {
        'feature1': {'mean': 22.5, 'median': 20.0, 'mode': 20, 'variance': 62.5},
        'feature2': {'mean': 30.0, 'median': 40.0, 'mode': 40, 'variance': 62.5},
        'feature3': {'mean': 4.0, 'median': 4.0, 'mode': 4, 'variance': 2.0},
        'feature4': {'mean': 4.0, 'median': 4.0, 'mode': 4, 'variance': 2.0},
        'feature5': {'mean': 3.0, 'median': 3.0, 'mode': 3, 'variance': 0.0}
    }
    
    result = task_func(sample_df, replacement_dict)
    assert result == expected_output

def test_task_func_invalid_input():
    invalid_df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    replacement_dict = {'feature3': {1: 10}}
    
    result = task_func(invalid_df, replacement_dict)
    assert result == "Invalid input"