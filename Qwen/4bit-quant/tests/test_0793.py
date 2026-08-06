import pandas as pd
import pytest
from src_0793 import task_func


def test_task_func_with_valid_data():
    # Create a sample DataFrame
    data = {
        'feature': [1, 2, 3, 4, 5],
        'target': [2, 3, 5, 7, 11]
    }
    df = pd.DataFrame(data)
    
    # Call the function with valid inputs
    result_indices, model = task_func(df, 'feature', 'target')
    
    # Check if the result is of the correct type
    assert isinstance(result_indices, list)
    assert isinstance(model, LinearRegression)
    
    # Check if the result indices are within the valid range
    assert all(0 <= idx < len(df) for idx in result_indices)

def test_task_func_with_missing_feature_column():
    # Create a sample DataFrame with missing feature column
    data = {
        'feature': [1, 2, 3, 4, 5],
        'target': [2, 3, 5, 7, 11]
    }
    df = pd.DataFrame(data)
    
    # Call the function with missing feature column
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 'missing_feature', 'target')
    
    # Check if the correct error message is raised
    assert str(excinfo.value) == "Columns missing_feature or target not found in the DataFrame."

def test_task_func_with_missing_target_column():
    # Create a sample DataFrame with missing target column
    data = {
        'feature': [1, 2, 3, 4, 5],
        'target': [2, 3, 5, 7, 11]
    }
    df = pd.DataFrame(data)
    
    # Call the function with missing target column
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 'feature', 'missing_target')
    
    # Check if the correct error message is raised
    assert str(excinfo.value) == "Columns feature or missing_target not found in the DataFrame."

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Call the function with empty DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 'feature', 'target')
    
    # Check if the correct error message is raised
    assert str(excinfo.value) == "Columns feature or target not found in the DataFrame."

def test_task_func_with_n_larger_than_dataframe_length():
    # Create a sample DataFrame
    data = {
        'feature': [1, 2, 3],
        'target': [2, 3, 5]
    }
    df = pd.DataFrame(data)
    
    # Call the function with n larger than the length of the DataFrame
    result_indices, model = task_func(df, 'feature', 'target', n=10)
    
    # Check if the result indices are within the valid range
    assert all(0 <= idx < len(df) for idx in result_indices)