import pytest
from src_0222 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'feature3': [2, 3, 4, 5, 6],
        'feature4': [6, 5, 4, 3, 2],
        'feature5': [3, 4, 5, 6, 7]
    }
    return pd.DataFrame(data)

@pytest.fixture
def replacement_dict():
    return {1: 10, 2: 20, 3: 30}

def test_task_func(sample_df, replacement_dict):
    result = task_func(sample_df, replacement_dict)
    
    # Expected means after replacement
    expected_means = {
        'feature1': 30.0,
        'feature2': 20.0,
        'feature3': 40.0,
        'feature4': 50.0,
        'feature5': 60.0
    }
    
    # Check if means are calculated correctly
    for feature, stats_dict in result.items():
        assert np.isclose(stats_dict['mean'], expected_means[feature])

def test_task_func_invalid_input():
    invalid_df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    result = task_func(invalid_df, {})
    assert result == "Invalid input"

def test_task_func_no_replacement(sample_df):
    result = task_func(sample_df, {})
    
    # Expected means without replacement
    expected_means = {
        'feature1': 3.0,
        'feature2': 3.0,
        'feature3': 4.0,
        'feature4': 4.0,
        'feature5': 5.0
    }
    
    # Check if means are calculated correctly
    for feature, stats_dict in result.items():
        assert np.isclose(stats_dict['mean'], expected_means[feature])

def test_task_func_with_mode(sample_df, replacement_dict):
    result = task_func(sample_df, replacement_dict)
    
    # Expected modes after replacement
    expected_modes = {
        'feature1': 10,
        'feature2': 20,
        'feature3': 30,
        'feature4': 40,
        'feature5': 50
    }
    
    # Check if modes are calculated correctly
    for feature, stats_dict in result.items():
        assert stats_dict['mode'] == expected_modes[feature]