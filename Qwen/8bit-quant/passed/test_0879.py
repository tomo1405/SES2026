import pytest
from src_0879 import task_func
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def test_task_func_with_valid_data():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    mse, model, returned_data = task_func(df, 'target')
    
    # Check if the returned DataFrame is the same as the input DataFrame
    assert returned_data.equals(df)
    
    # Check if the model is an instance of RandomForestRegressor
    assert isinstance(model, RandomForestRegressor)
    
    # Check if the MSE is a non-negative number
    assert mse >= 0

def test_task_func_with_empty_data():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="Data must not be empty and target column must exist in the DataFrame."):
        task_func(df, 'target')

def test_task_func_with_missing_target():
    # Create a DataFrame without the target column
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    
    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="Data must not be empty and target column must exist in the DataFrame."):
        task_func(df, 'target')

def test_task_func_with_custom_test_size():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    
    # Call the function with a custom test size
    mse, model, returned_data = task_func(df, 'target', test_size=0.5)
    
    # Check if the returned DataFrame is the same as the input DataFrame
    assert returned_data.equals(df)
    
    # Check if the model is an instance of RandomForestRegressor
    assert isinstance(model, RandomForestRegressor)
    
    # Check if the MSE is a non-negative number
    assert mse >= 0

def test_task_func_with_random_state():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    
    # Call the function with a random state
    mse1, model1, _ = task_func(df, 'target', random_state=42)
    mse2, model2, _ = task_func(df, 'target', random_state=42)
    
    # Check if the MSEs are the same
    assert mse1 == mse2
    
    # Check if the models are instances of RandomForestRegressor
    assert isinstance(model1, RandomForestRegressor)
    assert isinstance(model2, RandomForestRegressor)