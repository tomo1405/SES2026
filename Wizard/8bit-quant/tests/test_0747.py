python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pytest

def task_func(df, target_column, target_values=None):

    if not isinstance(df, pd.DataFrame):
        raise ValueError("df should be a DataFrame.")
    
    if df.empty:
        raise ValueError("df should contain at least one row")
    
    if target_column not in df.columns:
        raise ValueError("target_column should be in DataFrame")
    
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise ValueError("df values should be numeric only")

    if target_values != None:
        df = df.applymap(lambda x: x if x in target_values else 0)

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    model = LinearRegression().fit(X, y)

    return model

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
        model = task_func(df, target_column, target_values)

    # Test case 3: Invalid input - df is empty
    df = pd.DataFrame()
    target_column = 'C'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        model = task_func(df, target_column, target_values)

    # Test case 4: Invalid input - target_column not in df
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'D'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        model = task_func(df, target_column, target_values)

    # Test case 5: Invalid input - df values are not numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': ['7', '8', '9']})
    target_column = 'C'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        model = task_func(df, target_column, target_values)

    # Test case 6: Invalid input - target_values contains values not in df
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    target_values = [7, 8, 10]
    with pytest.raises(ValueError):
        model = task_func(df, target_column, target_values)