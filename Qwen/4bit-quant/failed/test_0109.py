import pytest
from src_0109 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = {
        'group': ['A', 'A', 'A', 'B', 'B', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=6, freq='D'),
        'value': [10, 20, 30, 40, 50, 60]
    }
    df = pd.DataFrame(data)

    # Call the function
    result, ax = task_func(df, freq='D', decomposition_model='multiplicative')

    # Check the type of the result
    assert isinstance(result, pd.DataFrame)

    # Check the type of the plot axis
    assert isinstance(ax, plt.Axes)

def test_task_func_missing_column():
    # Create a sample DataFrame without 'value' column
    data = {
        'group': ['A', 'A', 'A', 'B', 'B', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=6, freq='D')
    }
    df = pd.DataFrame(data)

    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns."):
        task_func(df)

def test_task_func_invalid_decomposition_model():
    # Create a sample DataFrame
    data = {
        'group': ['A', 'A', 'A', 'B', 'B', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=6, freq='D'),
        'value': [10, 20, 30, 40, 50, 60]
    }
    df = pd.DataFrame(data)

    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="Invalid 'decomposition_model': must be 'additive' or 'multiplicative'."):
        task_func(df, decomposition_model='invalid')

def test_task_func_non_numeric_value():
    # Create a sample DataFrame with non-numeric 'value'
    data = {
        'group': ['A', 'A', 'A', 'B', 'B', 'B'],
        'date': pd.date_range(start='2023-01-01', periods=6, freq='D'),
        'value': [10, 'not a number', 30, 40, 50, 60]
    }
    df = pd.DataFrame(data)

    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="Non-numeric or missing values found in 'value' column."):
        task_func(df)