import pytest
from src_0909 import task_func
import os
import pandas as pd
import re
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

# Mocking os.listdir and pd.read_csv to avoid file system access and data reading
@patch('src_0909.os.listdir')
@patch('src_0909.pd.read_csv')
def test_task_func(mock_read_csv, mock_listdir):
    # Mock os.listdir to return a list of files
    mock_listdir.return_value = ['file1.csv', 'file2.txt', 'file3.csv']
    
    # Mock pd.read_csv to return a DataFrame
    mock_df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar'],
        'Sales': [100, 200, 300]
    })
    mock_read_csv.return_value = mock_df
    
    # Define the directory and pattern
    directory = '/test/directory'
    pattern = r'^file\d+\.csv$'
    
    # Call the function
    plots = task_func(directory, pattern)
    
    # Assert that os.listdir was called with the correct directory
    mock_listdir.assert_called_once_with(directory)
    
    # Assert that pd.read_csv was called twice (for file1.csv and file3.csv)
    mock_read_csv.assert_any_call(os.path.join(directory, 'file1.csv'))
    mock_read_csv.assert_any_call(os.path.join(directory, 'file3.csv'))
    
    # Assert that the number of plots is correct
    assert len(plots) == 2
    
    # Assert that each plot is an AxesSubplot object
    for ax in plots:
        assert isinstance(ax, plt.Axes)

# Additional test to check behavior with no matching files
@patch('src_0909.os.listdir')
@patch('src_0909.pd.read_csv')
def test_task_func_no_matches(mock_read_csv, mock_listdir):
    # Mock os.listdir to return a list of files
    mock_listdir.return_value = ['file1.txt', 'file2.txt']
    
    # Define the directory and pattern
    directory = '/test/directory'
    pattern = r'^file\d+\.csv$'
    
    # Call the function
    plots = task_func(directory, pattern)
    
    # Assert that os.listdir was called with the correct directory
    mock_listdir.assert_called_once_with(directory)
    
    # Assert that pd.read_csv was not called
    mock_read_csv.assert_not_called()
    
    # Assert that the number of plots is zero
    assert len(plots) == 0