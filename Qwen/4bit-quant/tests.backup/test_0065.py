import pytest
from src_0065 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 5],
        [2, 1, 6],
        [2, 1, 7]
    ]

def test_task_func(sample_data):
    result_df, ax = task_func(sample_data)
    
    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)
    
    # Check if the DataFrame has the correct shape
    expected_shape = (2, 2)  # Based on the sample data
    assert result_df.shape == expected_shape
    
    # Check if the heatmap axis object is created
    assert isinstance(ax, plt.Axes)
    
    # Check if the DataFrame contains the correct values
    expected_values = np.array([[2, 1], [1, 2]])
    assert np.array_equal(result_df.values, expected_values)

def test_task_func_with_empty_data():
    empty_data = []
    result_df, ax = task_func(empty_data)
    
    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)
    
    # Check if the DataFrame is empty
    assert result_df.empty
    
    # Check if the heatmap axis object is created
    assert isinstance(ax, plt.Axes)

def test_task_func_with_single_row():
    single_row_data = [[1, 2, 3]]
    result_df, ax = task_func(single_row_data)
    
    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)
    
    # Check if the DataFrame has the correct shape
    expected_shape = (1, 1)
    assert result_df.shape == expected_shape
    
    # Check if the heatmap axis object is created
    assert isinstance(ax, plt.Axes)
    
    # Check if the DataFrame contains the correct values
    expected_values = np.array([[1]])
    assert np.array_equal(result_df.values, expected_values)