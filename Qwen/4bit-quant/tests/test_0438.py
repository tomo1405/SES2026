import pytest
from src_0438 import task_func
import pandas as pd
import os

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Call the function
    result_df = task_func(df)

    # Check if the result is the same as the input DataFrame
    assert result_df.equals(df)

    # Check if the file was not created on disk
    file_name = "save.pkl"
    assert not os.path.exists(file_name)

def test_task_func_with_custom_file_name():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Define a custom file name
    custom_file_name = "custom_save.pkl"

    # Call the function with the custom file name
    result_df = task_func(df, file_name=custom_file_name)

    # Check if the result is the same as the input DataFrame
    assert result_df.equals(df)

    # Check if the custom file was not created on disk
    assert not os.path.exists(custom_file_name)