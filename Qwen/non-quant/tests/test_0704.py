import pytest
from src_0704 import task_func
import pandas as pd
from sklearn.cluster import DBSCAN

def test_task_func():
    # Test with a simple dataset
    data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]
    cols = ['Feature1', 'Feature2']
    
    # Expected output after applying DBSCAN
    expected_output = pd.DataFrame({
        'Feature1': [1, 2, 2, 8, 8, 25],
        'Feature2': [2, 2, 3, 7, 8, 80],
        'Cluster': [-1, -1, -1, -1, -1, 1]
    })
    
    # Call the function
    result_df = task_func(data, cols)
    
    # Check if the resulting DataFrame matches the expected output
    assert result_df.equals(expected_output), "The output DataFrame does not match the expected output."

def test_task_func_empty_data():
    # Test with empty data
    data = []
    cols = ['Feature1', 'Feature2']
    
    # Expected output is an empty DataFrame with the specified columns
    expected_output = pd.DataFrame(columns=['Feature1', 'Feature2', 'Cluster'])
    
    # Call the function
    result_df = task_func(data, cols)
    
    # Check if the resulting DataFrame matches the expected output
    assert result_df.equals(expected_output), "The output DataFrame does not match the expected output for empty data."

def test_task_func_single_column():
    # Test with a single column of data
    data = [[1], [2], [3]]
    cols = ['Feature1']
    
    # Expected output after applying DBSCAN
    expected_output = pd.DataFrame({
        'Feature1': [1, 2, 3],
        'Cluster': [-1, -1, -1]
    })
    
    # Call the function
    result_df = task_func(data, cols)
    
    # Check if the resulting DataFrame matches the expected output
    assert result_df.equals(expected_output), "The output DataFrame does not match the expected output for a single column."