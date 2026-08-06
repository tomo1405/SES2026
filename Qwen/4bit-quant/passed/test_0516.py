import pytest
from src_0516 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_input():
    # Test with a valid input
    array = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6]
    ]
    df, heatmap = task_func(array)
    
    # Check if the DataFrame is created correctly
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (3, 5)
    
    # Check if the heatmap is created (non-null value check)
    assert heatmap is not None

def test_task_func_empty_input():
    # Test with an empty input
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func([])

def test_task_func_sublist_length_mismatch():
    # Test with sublists of different lengths
    array = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2],  # This sublist has only 4 elements
        [2, 3, 4, 5, 6]
    ]
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func(array)

def test_task_func_single_sublist():
    # Test with a single sublist
    array = [[1, 2, 3, 4, 5]]
    df, heatmap = task_func(array)
    
    # Check if the DataFrame is created correctly
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (1, 5)
    
    # Check if the heatmap is created (non-null value check)
    assert heatmap is not None

def test_task_func_identical_sublists():
    # Test with identical sublists
    array = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ]
    df, heatmap = task_func(array)
    
    # Check if the DataFrame is created correctly
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (3, 5)
    
    # Check if the heatmap is created (non-null value check)
    assert heatmap is not None

def test_task_func_random_data():
    # Test with random data
    np.random.seed(0)
    array = np.random.randint(0, 100, size=(4, 5)).tolist()
    df, heatmap = task_func(array)
    
    # Check if the DataFrame is created correctly
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (4, 5)
    
    # Check if the heatmap is created (non-null value check)
    assert heatmap is not None