import pytest
from src_0516 import task_func
import pandas as pd

def test_task_func_valid_input():
    # Test with a valid input
    input_array = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6]
    ]
    df, heatmap = task_func(input_array)
    
    # Check if the DataFrame is created correctly
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (3, 5)
    
    # Check if the heatmap is created
    assert isinstance(heatmap, sns.axisgrid.heatmap)

def test_task_func_empty_input():
    # Test with an empty input
    input_array = []
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func(input_array)

def test_task_func_sublist_length_mismatch():
    # Test with a sublist of incorrect length
    input_array = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2],  # This sublist has only 4 elements
        [2, 3, 4, 5, 6]
    ]
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func(input_array)

def test_task_func_single_element_sublist():
    # Test with a single element sublist
    input_array = [
        [1, 2, 3, 4, 5],
        [5],  # This sublist has only 1 element
        [2, 3, 4, 5, 6]
    ]
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func(input_array)