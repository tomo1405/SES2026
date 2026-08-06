import pytest
from src_0704 import task_func
import pandas as pd
from sklearn.cluster import DBSCAN

def test_task_func():
    # Test with simple data
    data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]
    cols = ['Feature1', 'Feature2']
    result_df = task_func(data, cols)
    
    # Check if the returned object is a DataFrame
    assert isinstance(result_df, pd.DataFrame)
    
    # Check if the DataFrame has the correct columns
    expected_columns = cols + ['Cluster']
    assert list(result_df.columns) == expected_columns
    
    # Check if the DataFrame has the correct number of rows
    assert len(result_df) == len(data)
    
    # Check if the 'Cluster' column exists and is of integer type
    assert 'Cluster' in result_df.columns
    assert result_df['Cluster'].dtype == int
    
    # Check if the DBSCAN algorithm is applied correctly
    # This is a basic check to ensure that clusters are formed
    unique_clusters = result_df['Cluster'].unique()
    assert len(unique_clusters) > 1  # Expect more than one cluster (including noise)

def test_task_func_empty_data():
    # Test with empty data
    data = []
    cols = ['Feature1', 'Feature2']
    result_df = task_func(data, cols)
    
    # Check if the returned object is a DataFrame
    assert isinstance(result_df, pd.DataFrame)
    
    # Check if the DataFrame has the correct columns
    expected_columns = cols + ['Cluster']
    assert list(result_df.columns) == expected_columns
    
    # Check if the DataFrame is empty
    assert result_df.empty

def test_task_func_single_row():
    # Test with a single row of data
    data = [[1, 2]]
    cols = ['Feature1', 'Feature2']
    result_df = task_func(data, cols)
    
    # Check if the returned object is a DataFrame
    assert isinstance(result_df, pd.DataFrame)
    
    # Check if the DataFrame has the correct columns
    expected_columns = cols + ['Cluster']
    assert list(result_df.columns) == expected_columns
    
    # Check if the DataFrame has the correct number of rows
    assert len(result_df) == len(data)
    
    # Check if the 'Cluster' column exists and is of integer type
    assert 'Cluster' in result_df.columns
    assert result_df['Cluster'].dtype == int
    
    # Check if the DBSCAN algorithm is applied correctly
    # This is a basic check to ensure that clusters are formed
    unique_clusters = result_df['Cluster'].unique()
    assert len(unique_clusters) == 1  # Expect only one cluster (noise)