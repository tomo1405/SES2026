python
import heapq
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from src_0793 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [5, 4, 3, 2, 1]})
    feature = 'feature'
    target = 'target'
    n = 3
    expected_result = ([2, 3, 4], LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False))
    result = task_func(df, feature, target, n)
    assert result == expected_result

    # Test case 2: Invalid input (feature column not found)
    df = pd.DataFrame({'target': [5, 4, 3, 2, 1]})
    feature = 'feature'
    target = 'target'
    n = 3
    with pytest.raises(ValueError):
        task_func(df, feature, target, n)

    # Test case 3: Invalid input (target column not found)
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5]})
    feature = 'feature'
    target = 'target'
    n = 3
    with pytest.raises(ValueError):
        task_func(df, feature, target, n)

    # Test case 4: Invalid input (n is not a positive integer)
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [5, 4, 3, 2, 1]})
    feature = 'feature'
    target = 'target'
    n = 0
    with pytest.raises(ValueError):
        task_func(df, feature, target, n)

    # Test case 5: Invalid input (n is greater than the number of rows in the dataframe)
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [5, 4, 3, 2, 1]})
    feature = 'feature'
    target = 'target'
    n = 100
    with pytest.raises(ValueError):
        task_func(df, feature, target, n)