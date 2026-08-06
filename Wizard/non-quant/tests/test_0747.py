python
import numpy as np
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from src_0747 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    target_values = [7, 8, 9]
    model = task_func(df, target_column, target_values)
    assert isinstance(model, LinearRegression)

    # Test case 2: Invalid input - df is not a DataFrame
    df = [1, 2, 3]
    target_column = 'C'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)

    # Test case 3: Invalid input - df is empty
    df = pd.DataFrame()
    target_column = 'C'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)

    # Test case 4: Invalid input - target_column not in df
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'D'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)

    # Test case 5: Invalid input - df values are not numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': ['7', '8', '9']})
    target_column = 'C'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)

    # Test case 6: Invalid input - target_values contains values not in df
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    target_values = [7, 8, 10]
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)