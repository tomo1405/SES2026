import pandas as pd
from sklearn.linear_model import LinearRegression
import pytest

def task_func(df):
    X = pd.DataFrame(df[['X']])  # Extracting column 'X' as a DataFrame
    y = pd.Series(df['Y'])       # Extracting column 'Y' as a Series
    
    # Fitting the linear regression model
    model = LinearRegression().fit(X, y)
    
    return model

def test_task_func():
    # Creating a sample DataFrame for testing
    df = pd.DataFrame({
        'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 6, 8, 10]
    })
    
    # Expected output
    expected_model = LinearRegression().fit(df[['X']], df['Y'])
    
    # Calling the function under test
    result_model = task_func(df)
    
    # Asserting that the function returns the expected output
    assert result_model.coef_[0] == expected_model.coef_[0]
    assert result_model.intercept_ == expected_model.intercept_