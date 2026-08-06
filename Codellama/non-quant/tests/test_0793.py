import pandas as pd
import pytest
from src_0793 import task_func


def test_task_func():
    # Test case 1: Ensure provided columns exist in the dataframe
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [10, 20, 30, 40, 50]})
    feature = 'feature'
    target = 'target'
    n = 10
    with pytest.raises(ValueError):
        task_func(df, 'invalid_feature', target, n)
    with pytest.raises(ValueError):
        task_func(df, feature, 'invalid_target', n)

    # Test case 2: Ensure the function returns the correct residuals and model
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [10, 20, 30, 40, 50]})
    feature = 'feature'
    target = 'target'
    n = 10
    largest_residual_indices, model = task_func(df, feature, target, n)
    assert len(largest_residual_indices) == n
    assert isinstance(model, LinearRegression)
    assert model.coef_[0] == pytest.approx(1)
    assert model.intercept_ == pytest.approx(0)