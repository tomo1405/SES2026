import pytest
from src_0885 import task_func
import pandas as pd

# Test case 1: Basic functionality with valid input
def test_task_func_basic():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 20, 30, 40, 50],
        'C': [500, 900, 500, 900, 500]
    }
    df = pd.DataFrame(data)
    p_value = task_func(df)
    assert isinstance(p_value, float)

# Test case 2: Invalid number of columns
def test_task_func_invalid_columns():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 20, 30, 40, 50],
        'C': [500, 900, 500, 900, 500]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Exactly three columns should be specified."):
        task_func(df, columns=['A', 'B'])

# Test case 3: Non-existent column
def test_task_func_non_existent_column():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 20, 30, 40, 50],
        'C': [500, 900, 500, 900, 500]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="The specified columns should exist in the DataFrame."):
        task_func(df, columns=['A', 'B', 'D'])

# Test case 4: Insufficient data
def test_task_func_insufficient_data():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 20, 30, 40, 50],
        'C': [500, 500, 500, 500, 500]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Insufficient data - no matching data for the applied conditions."):
        task_func(df)

# Test case 5: Different threshold values
def test_task_func_different_thresholds():
    data = {
        'A': ['X', 'Y', 'X', 'Z', 'Y'],
        'B': [10, 20, 30, 40, 50],
        'C': [500, 900, 500, 900, 500]
    }
    df = pd.DataFrame(data)
    p_value = task_func(df, larger=15, equal=500)
    assert isinstance(p_value, float)

# Test case 6: Empty DataFrame
def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="Exactly three columns should be specified."):
        task_func(df)