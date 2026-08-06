import pytest
from src_0866 import task_func
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Sample data
    data = [
        ('item1', 10, 20),
        ('item2', 20, 30),
        ('item3', 30, 40)
    ]
    
    # Expected output
    expected_items = ['item1', 'item2', 'item3']
    expected_counts = zscore([10, 20, 30])
    scaler = MinMaxScaler()
    expected_weights = scaler.fit_transform(np.array([20, 30, 40]).reshape(-1, 1)).flatten()
    
    # Create expected DataFrame
    expected_df = pd.DataFrame({
        'Item': expected_items,
        'Normalized Count': expected_counts,
        'Normalized Weight': expected_weights
    })
    
    # Actual output
    actual_df = task_func(data)
    
    # Check if the DataFrames are equal
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_empty_data():
    # Test with empty data
    data = []
    
    # Expected output is an empty DataFrame
    expected_df = pd.DataFrame(columns=['Item', 'Normalized Count', 'Normalized Weight'])
    
    # Actual output
    actual_df = task_func(data)
    
    # Check if the DataFrames are equal
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_single_item():
    # Test with a single item
    data = [('item1', 10, 20)]
    
    # Expected output
    expected_items = ['item1']
    expected_counts = zscore([10])
    scaler = MinMaxScaler()
    expected_weights = scaler.fit_transform(np.array([20]).reshape(-1, 1)).flatten()
    
    # Create expected DataFrame
    expected_df = pd.DataFrame({
        'Item': expected_items,
        'Normalized Count': expected_counts,
        'Normalized Weight': expected_weights
    })
    
    # Actual output
    actual_df = task_func(data)
    
    # Check if the DataFrames are equal
    pd.testing.assert_frame_equal(actual_df, expected_df)