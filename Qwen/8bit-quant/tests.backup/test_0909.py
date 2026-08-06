import pytest
from src_0909 import task_func
import os
import pandas as pd
import re
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

# Mocking os.listdir to simulate directory contents
@patch('os.listdir')
# Mocking pd.read_csv to simulate reading CSV files
@patch('pandas.read_csv')
# Mocking plt.show to prevent actual plotting
@patch('matplotlib.pyplot.show')
def test_task_func(mock_show, mock_read_csv, mock_listdir):
    # Setup mock data
    mock_listdir.return_value = ['file1.csv', 'file2.csv']
    mock_read_csv.side_effect = [
        pd.DataFrame({'Month': ['Jan', 'Feb'], 'Sales': [100, 200]}),
        pd.DataFrame({'Month': ['Mar', 'Apr'], 'Sales': [300, 400]})
    ]
    
    # Define test parameters
    directory = '/test/directory'
    pattern = r'^file\d\.csv$'
    
    # Call the function
    result = task_func(directory, pattern)
    
    # Assertions
    assert len(result) == 2, "Expected two plots"
    assert isinstance(result[0], plt.Axes), "First element should be a matplotlib Axes object"
    assert isinstance(result[1], plt.Axes), "Second element should be a matplotlib Axes object"
    
    # Verify that pd.read_csv was called twice with correct paths
    mock_read_csv.assert_any_call(os.path.join(directory, 'file1.csv'))
    mock_read_csv.assert_any_call(os.path.join(directory, 'file2.csv'))
    
    # Verify that plt.show was called
    mock_show.assert_called_once()

# Test case for no matching files
@patch('os.listdir')
@patch('pandas.read_csv')
@patch('matplotlib.pyplot.show')
def test_task_func_no_matching_files(mock_show, mock_read_csv, mock_listdir):
    # Setup mock data
    mock_listdir.return_value = ['file1.txt', 'file2.csv']
    
    # Define test parameters
    directory = '/test/directory'
    pattern = r'^file\d\.csv$'
    
    # Call the function
    result = task_func(directory, pattern)
    
    # Assertions
    assert len(result) == 0, "Expected no plots"
    
    # Verify that pd.read_csv was not called
    mock_read_csv.assert_not_called()
    
    # Verify that plt.show was not called
    mock_show.assert_not_called()