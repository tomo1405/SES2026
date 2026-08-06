import pytest
from src_0690 import task_func
import pandas as pd
import numpy as np
from scipy import stats

def test_task_func_with_normal_data():
    # Create a DataFrame with normally distributed data
    data = {
        'A': np.random.normal(loc=0, scale=1, size=100),
        'B': np.random.normal(loc=0, scale=1, size=100),
        'C': np.random.normal(loc=0, scale=1, size=100)
    }
    df = pd.DataFrame(data)
    
    # Expected: All p-values should be greater than 0.05 (assuming normality)
    p_values = task_func(df)
    
    for p_value in p_values.values():
        assert p_value > 0.05, f"p-value {p_value} is not greater than 0.05"

def test_task_func_with_non_normal_data():
    # Create a DataFrame with non-normally distributed data
    data = {
        'A': np.random.exponential(scale=1, size=100),
        'B': np.random.exponential(scale=1, size=100),
        'C': np.random.exponential(scale=1, size=100)
    }
    df = pd.DataFrame(data)
    
    # Expected: At least one p-value should be less than 0.05 (rejecting normality)
    p_values = task_func(df)
    
    for p_value in p_values.values():
        assert p_value < 0.05, f"p-value {p_value} is not less than 0.05"

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Expected: An empty dictionary should be returned
    p_values = task_func(df)
    
    assert p_values == {}, "Expected an empty dictionary for an empty DataFrame"

def test_task_func_with_single_column():
    # Create a DataFrame with a single column of normally distributed data
    data = {'A': np.random.normal(loc=0, scale=1, size=100)}
    df = pd.DataFrame(data)
    
    # Expected: A dictionary with a single key-value pair
    p_values = task_func(df)
    
    assert len(p_values) == 1, "Expected a dictionary with a single key-value pair"
    assert 'A' in p_values, "Expected the key 'A' in the dictionary"
    assert p_values['A'] > 0.05, f"p-value {p_values['A']} is not greater than 0.05"

def test_task_func_with_all_identical_values():
    # Create a DataFrame with a single column of identical values
    data = {'A': np.full(100, 1)}
    df = pd.DataFrame(data)
    
    # Expected: A dictionary with a single key-value pair where p-value is NaN or very low
    p_values = task_func(df)
    
    assert len(p_values) == 1, "Expected a dictionary with a single key-value pair"
    assert 'A' in p_values, "Expected the key 'A' in the dictionary"
    assert np.isnan(p_values['A']) or p_values['A'] < 0.05, f"p-value {p_values['A']} is not NaN or less than 0.05"