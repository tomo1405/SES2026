import pandas as pd
from sklearn.linear_model import LinearRegression
import pytest

ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    X = pd.DataFrame(df[['X']])  # Extracting column 'X' as a DataFrame
    y = pd.Series(df['Y'])       # Extracting column 'Y' as a Series
    
    # Fitting the linear regression model
    model = LinearRegression().fit(X, y)
    
    return model

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'X': range(ROWS),
        'Y': range(ROWS)
    })
    
    # Call the function and store the result
    result = task_func(df)
    
    # Assert that the result is an instance of LinearRegression
    assert isinstance(result, LinearRegression)
    
    # Assert that the model has been fitted
    assert result.coef_.size > 0
    
    # Assert that the model's predictions match the expected values
    X_test = pd.DataFrame(df[['X']])
    y_pred = result.predict(X_test)
    assert (y_pred == df['Y']).all()