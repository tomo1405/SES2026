import pytest
from src_0141 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Test cases for the task_func function

def test_task_func_valid_input():
    # Test with valid input
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    cols = ['A']
    result = task_func(df, cols)
    assert result['A'].equals(pd.Series([-1.224744871391589, 0.0, 1.224744871391589]))

def test_task_func_invalid_df():
    # Test with invalid df type
    df = "not a DataFrame"
    cols = ['A']
    with pytest.raises(ValueError):
        task_func(df, cols)

def test_task_func_invalid_cols():
    # Test with invalid cols type
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    cols = "not a list"
    with pytest.raises(ValueError):
        task_func(df, cols)

def test_task_func_missing_columns():
    # Test with missing columns
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    cols = ['A', 'C']
    with pytest.raises(ValueError):
        task_func(df, cols)

def test_task_func_scaler_transform():
    # Test the scaling transformation
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    cols = ['A']
    result = task_func(df, cols)
    assert result['A'].equals(pd.Series([-1.224744871391589, 0.0, 1.224744871391589]))