import pandas as pd
import pytest
from src_0793 import task_func


def test_task_func():
    # Test case 1: Ensure provided columns exist in the dataframe
    df = pd.DataFrame({'feature': [1, 2, 3], 'target': [4, 5, 6]})
    feature = 'feature'
    target = 'target'
    n = 10
    with pytest.raises(ValueError):
        task_func(df, 'invalid_feature', target, n)
    with pytest.raises(ValueError):
        task_func(df, feature, 'invalid_target', n)

    # Test case 2: Ensure the function returns the correct output
    df = pd.DataFrame({'feature': [1, 2, 3], 'target': [4, 5, 6]})
    feature = 'feature'
    target = 'target'
    n = 10
    largest_residual_indices, model = task_func(df, feature, target, n)
    assert len(largest_residual_indices) == n
    assert isinstance(model, LinearRegression)

    # Test case 3: Ensure the function handles missing values correctly
    df = pd.DataFrame({'feature': [1, 2, 3], 'target': [4, 5, 6]})
    feature = 'feature'
    target = 'target'
    n = 10
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    largest_residual_indices, model = task_func(df, feature, target, n)
    assert len(largest_residual_indices) == n
    assert isinstance(model, LinearRegression)

    # Test case 4: Ensure the function handles duplicate values correctly
    df = pd.DataFrame({'feature': [1, 2, 3], 'target': [4, 5, 6]})
    feature = 'feature'
    target = 'target'
    n = 10
    df.iloc[0, 0] = 1
    df.iloc[1, 1] = 1
    largest_residual_indices, model = task_func(df, feature, target, n)
    assert len(largest_residual_indices) == n
    assert isinstance(model, LinearRegression)