import pandas as pd
from sklearn.linear_model import LinearRegression
import pytest

def task_func(df, target):
    X = pd.DataFrame.drop(df, target, axis=1)  
    y = pd.Series(df[target])  
    
    model = LinearRegression()
    model.fit(X, y)

    return model.score(X, y)

def test_task_func():
    # Create a sample DataFrame and target variable for testing
    df = pd.DataFrame({'x1': [1, 2, 3], 'x2': [4, 5, 6], 'y': [7, 8, 9]})
    target = 'y'

    # Call the function and store the result
    result = task_func(df, target)

    # Define the expected result
    expected_result = 1.0

    # Use pytest.approx to compare the result with the expected result
    assert result == pytest.approx(expected_result)