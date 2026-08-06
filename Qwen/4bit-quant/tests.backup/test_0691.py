import pytest
from src_0691 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_with_valid_data():
    # Create a sample DataFrame with valid data
    data = {
        'X': range(100),
        'Y': [2 * x + 1 for x in range(100)]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    model = task_func(df)
    
    # Check if the model is an instance of LinearRegression
    assert isinstance(model, LinearRegression)
    
    # Check if the model has been fitted
    assert model.coef_ is not None and model.intercept_ is not None

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['X', 'Y'])
    
    # Call the function
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_with_missing_column():
    # Create a DataFrame missing one of the required columns
    data = {
        'X': range(100)
    }
    df = pd.DataFrame(data)
    
    # Call the function
    with pytest.raises(KeyError):
        task_func(df)

def test_task_func_with_non_numeric_data():
    # Create a DataFrame with non-numeric data
    data = {
        'X': ['a', 'b', 'c'],
        'Y': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    with pytest.raises(ValueError):
        task_func(df)