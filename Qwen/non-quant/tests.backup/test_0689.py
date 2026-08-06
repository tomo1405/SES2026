import pytest
from src_0689 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    # Expected result after standardization
    scaler = StandardScaler()
    expected_data = scaler.fit_transform(df)
    expected_df = pd.DataFrame(expected_data, columns=df.columns)
    
    # Get the result from the function
    result_df = task_func(df)
    
    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_empty_df():
    # Test with an empty DataFrame
    df = pd.DataFrame()
    
    # The function should return an empty DataFrame
    result_df = task_func(df)
    
    assert result_df.empty

def test_task_func_single_column():
    # Test with a DataFrame having a single column
    data = {
        'A': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    
    # Expected result after standardization
    scaler = StandardScaler()
    expected_data = scaler.fit_transform(df)
    expected_df = pd.DataFrame(expected_data, columns=df.columns)
    
    # Get the result from the function
    result_df = task_func(df)
    
    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_non_numeric_data():
    # Test with a DataFrame containing non-numeric data
    data = {
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    with pytest.raises(ValueError):
        task_func(df)