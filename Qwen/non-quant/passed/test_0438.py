import pytest
from src_0438 import task_func
import pandas as pd
import os

def test_task_func_with_default_filename():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Call the function
    result_df = task_func(df)
    
    # Check if the result is the same as the input DataFrame
    assert result_df.equals(df)
    
    # Check if the file was removed
    assert not os.path.exists("save.pkl")

def test_task_func_with_custom_filename():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Define a custom filename
    custom_filename = "custom_save.pkl"
    
    # Call the function with the custom filename
    result_df = task_func(df, file_name=custom_filename)
    
    # Check if the result is the same as the input DataFrame
    assert result_df.equals(df)
    
    # Check if the file was removed
    assert not os.path.exists(custom_filename)

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Call the function
    result_df = task_func(df)
    
    # Check if the result is the same as the input DataFrame
    assert result_df.equals(df)
    
    # Check if the file was removed
    assert not os.path.exists("save.pkl")

def test_task_func_with_large_dataframe():
    # Create a large DataFrame
    df = pd.DataFrame({'A': range(1000), 'B': range(1000, 2000)})
    
    # Call the function
    result_df = task_func(df)
    
    # Check if the result is the same as the input DataFrame
    assert result_df.equals(df)
    
    # Check if the file was removed
    assert not os.path.exists("save.pkl")