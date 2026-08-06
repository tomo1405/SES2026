import pytest
from src_0202 import task_func
import pandas as pd
import numpy as np

def test_task_func_column_not_exists():
    df = pd.DataFrame({'A': [1, 2, 3]})
    with pytest.raises(ValueError, match="Column 'B' does not exist in DataFrame"):
        task_func(df, 'B', 2)

def test_task_func_value_not_number():
    df = pd.DataFrame({'A': [1, 2, 3]})
    with pytest.raises(ValueError, match="Value must be a number"):
        task_func(df, 'A', 'a')

def test_task_func_valid_data():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    greater_avg, num_greater_value, ax = task_func(df, 'A', 3)
    
    # Check if greater_avg is correct
    assert np.array_equal(greater_avg, np.array([4, 5]))
    
    # Check if num_greater_value is correct
    assert num_greater_value == 2
    
    # Check if ax is not None (assuming it's a valid plot object)
    assert ax is not None

def test_task_func_no_greater_than_average():
    df = pd.DataFrame({'A': [1, 2, 3]})
    greater_avg, num_greater_value, ax = task_func(df, 'A', 3)
    
    # Check if greater_avg is empty
    assert np.array_equal(greater_avg, np.array([]))
    
    # Check if num_greater_value is 0
    assert num_greater_value == 0
    
    # Check if ax is not None (assuming it's a valid plot object)
    assert ax is not None

def test_task_func_all_greater_than_value():
    df = pd.DataFrame({'A': [6, 7, 8]})
    greater_avg, num_greater_value, ax = task_func(df, 'A', 3)
    
    # Check if num_greater_value is equal to the length of the dataframe
    assert num_greater_value == 3
    
    # Check if ax is not None (assuming it's a valid plot object)
    assert ax is not None