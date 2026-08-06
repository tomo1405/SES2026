import pytest
from src_0685 import task_func
import pandas as pd
import numpy as np

def test_task_func_remove_column():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Expected result after removing column 'B'
    expected_data = {'A': [1, 2, 3]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'B')
    
    # Check if the column 'B' is removed
    assert 'B' not in result_df.columns
    # Check if the DataFrame content is correct
    pd.testing.assert_frame_equal(result_df.drop('IsEvenIndex', axis=1), expected_df)

def test_task_func_add_even_index_column():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Expected result after adding 'IsEvenIndex' column
    expected_data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'IsEvenIndex': [True, False, True]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'C')  # Column 'C' does not exist, so it should be ignored
    
    # Check if the 'IsEvenIndex' column is added correctly
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Expected result after processing
    expected_data = {'IsEvenIndex': []}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'A')  # Column 'A' does not exist, so it should be ignored
    
    # Check if the 'IsEvenIndex' column is added correctly
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_single_row_dataframe():
    # Create a single row DataFrame
    data = {'A': [1]}
    df = pd.DataFrame(data)
    
    # Expected result after processing
    expected_data = {'A': [1], 'IsEvenIndex': [True]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df, 'B')  # Column 'B' does not exist, so it should be ignored
    
    # Check if the 'IsEvenIndex' column is added correctly
    pd.testing.assert_frame_equal(result_df, expected_df)