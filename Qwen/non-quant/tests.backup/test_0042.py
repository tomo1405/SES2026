import pytest
from src_0042 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_output():
    # Create a sample data matrix
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Expected skewness calculation
    expected_skewness = [0.0, 0.0, 0.0]
    expected_df = pd.DataFrame(expected_skewness, columns=["Skewness"])
    
    # Call the function
    df, ax = task_func(data_matrix)
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Distribution of Skewness"
    assert len(ax.patches) == len(expected_skewness)

def test_task_func_empty_input():
    # Test with an empty data matrix
    data_matrix = np.array([])
    
    # Expected result
    expected_df = pd.DataFrame(columns=["Skewness"])
    
    # Call the function
    df, ax = task_func(data_matrix)
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Distribution of Skewness"
    assert len(ax.patches) == 0

def test_task_func_single_row():
    # Test with a single row data matrix
    data_matrix = np.array([[1, 2, 3]])
    
    # Expected skewness calculation
    expected_skewness = [0.0]
    expected_df = pd.DataFrame(expected_skewness, columns=["Skewness"])
    
    # Call the function
    df, ax = task_func(data_matrix)
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Distribution of Skewness"
    assert len(ax.patches) == len(expected_skewness)