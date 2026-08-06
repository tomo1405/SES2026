python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from src_0886 import task_func

def test_task_func():
    # Test case 1: Valid input dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [901, 902, 903, 904, 905]})
    predictions, model = task_func(df)
    assert isinstance(predictions, pd.Series)
    assert isinstance(model, LinearRegression)

    # Test case 2: Invalid input dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'D': [901, 902, 903, 904, 905]})
    predictions = task_func(df)
    assert predictions is None

    # Test case 3: Non-numeric data in input dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': ['901', '902', '903', '904', '905']})
    predictions = task_func(df)
    assert predictions is None

    # Test case 4: Empty dataframe
    df = pd.DataFrame({'A': [], 'B': [], 'C': []})
    predictions = task_func(df)
    assert predictions is None

    # Test case 5: No data points in selected dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [49, 50, 51, 52, 53], 'C': [901, 902, 903, 904, 905]})
    predictions = task_func(df)
    assert predictions is None

    # Test case 6: Test with seed
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [901, 902, 903, 904, 905]})
    predictions, model = task_func(df, seed=42)
    assert isinstance(predictions, pd.Series)
    assert isinstance(model, LinearRegression)