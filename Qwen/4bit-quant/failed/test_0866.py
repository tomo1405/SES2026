import pytest
from src_0866 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    return [
        ('item1', 10, 5),
        ('item2', 20, 10),
        ('item3', 30, 15)
    ]

def test_task_func(sample_data):
    result_df = task_func(sample_data)
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Item', 'Normalized Count', 'Normalized Weight']
    assert list(result_df.columns) == expected_columns
    
    # Check if the DataFrame has the correct number of rows
    assert len(result_df) == len(sample_data)
    
    # Check if the 'Item' column contains the correct values
    assert all(result_df['Item'] == [item for item, _, _ in sample_data])
    
    # Check if the 'Normalized Count' and 'Normalized Weight' are numeric
    assert np.all(np.isfinite(result_df['Normalized Count']))
    assert np.all(np.isfinite(result_df['Normalized Weight']))

def test_task_func_empty_input():
    result_df = task_func([])
    
    # Check if the DataFrame is empty
    assert result_df.empty
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Item', 'Normalized Count', 'Normalized Weight']
    assert list(result_df.columns) == expected_columns

def test_task_func_single_item():
    sample_data = [('item1', 10, 5)]
    result_df = task_func(sample_data)
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Item', 'Normalized Count', 'Normalized Weight']
    assert list(result_df.columns) == expected_columns
    
    # Check if the DataFrame has the correct number of rows
    assert len(result_df) == len(sample_data)
    
    # Check if the 'Item' column contains the correct value
    assert result_df['Item'].iloc[0] == sample_data[0][0]
    
    # Check if the 'Normalized Count' and 'Normalized Weight' are numeric
    assert np.isfinite(result_df['Normalized Count'].iloc[0])
    assert np.isfinite(result_df['Normalized Weight'].iloc[0])