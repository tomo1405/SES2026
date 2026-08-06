import pytest
from src_0691 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression


def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]})
    
    # Test that the function returns a LinearRegression model
    model = task_func(df)
    assert isinstance(model, LinearRegression)
    
    # Test that the model has the correct coefficients
    expected_coef = [1, 2]
    assert model.coef_ == expected_coef
    
    # Test that the model has the correct intercept
    expected_intercept = 0
    assert model.intercept_ == expected_intercept
    
    # Test that the model has the correct R-squared value
    expected_r2 = 1
    assert model.score(df[['X']], df['Y']) == expected_r2