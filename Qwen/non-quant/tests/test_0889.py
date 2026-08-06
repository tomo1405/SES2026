import pytest
from src_0889 import task_func
import pandas as pd
import os
from unittest.mock import patch

@patch('os.path.join')
@patch('pandas.read_csv')
def test_task_func(mock_read_csv, mock_os_join):
    # Mocking os.path.join to return a fixed path
    mock_os_join.return_value = 'mocked/path/to/file.csv'
    
    # Mocking pandas.read_csv to return a sample DataFrame
    sample_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    mock_read_csv.return_value = sample_df
    
    # Define the data directory and CSV files list
    data_dir = 'test_data'
    csv_files = ['file1.csv', 'file2.csv']
    
    # Expected result after merging two DataFrames
    expected_df = pd.concat([sample_df, sample_df], ignore_index=True)
    
    # Call the function
    result_df = task_func(data_dir, csv_files)
    
    # Assert that the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)
    
    # Assert that os.path.join was called correctly
    mock_os_join.assert_called_with(data_dir, 'file1.csv')
    mock_os_join.assert_called_with(data_dir, 'file2.csv')
    
    # Assert that pandas.read_csv was called correctly
    mock_read_csv.assert_called_with('mocked/path/to/file.csv')