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
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'X': range(100),
        'Y': range(100, 200)
    })
    
    # Call the function and store the result
    result = task_func(df)
    
    # Assert that the result is an instance of LinearRegression
    assert isinstance(result, LinearRegression)
    
    # Assert that the model has been fitted with the correct data
    assert result.coef_[0] == 1
    assert result.intercept_ == 0

if __name__ == '__main__':
    pytest.main()