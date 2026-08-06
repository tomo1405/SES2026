import pytest
from src_0149 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func_basic():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C']}
    df = pd.DataFrame(data)
    
    # Expected output after encoding
    expected_data = {'Category': [0, 1, 0, 2]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'Category')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_df)

def test_task_func_with_single_unique_value():
    # Create a sample DataFrame with a single unique value
    data = {'Category': ['A', 'A', 'A']}
    df = pd.DataFrame(data)
    
    # Expected output after encoding
    expected_data = {'Category': [0, 0, 0]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'Category')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_df)

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Call the function
    result_df = task_func(df, 'Category')
    
    # Check if the result is still an empty DataFrame
    assert result_df.empty

def test_task_func_with_nonexistent_column():
    # Create a sample DataFrame
    data = {'Category': ['A', 'B', 'A', 'C']}
    df = pd.DataFrame(data)
    
    # Expect a ValueError since the column does not exist
    with pytest.raises(KeyError):
        task_func(df, 'NonExistentColumn')

def test_task_func_with_numeric_column():
    # Create a sample DataFrame with a numeric column
    data = {'Number': [1, 2, 3, 4]}
    df = pd.DataFrame(data)
    
    # Expected output after encoding (should remain unchanged)
    expected_data = {'Number': [1, 2, 3, 4]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'Number')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_df)