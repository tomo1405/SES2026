import pytest
from src_0516 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_valid_input():
    array = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6]
    ]
    df, heatmap = task_func(array)
    
    # Check if DataFrame is created correctly
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (3, 5)
    
    # Check if heatmap is created
    assert isinstance(heatmap, plt.AxesImage)

def test_task_func_with_empty_input():
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func([])

def test_task_func_with_sublist_of_wrong_length():
    array = [
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6]
    ]
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func(array)

def test_task_func_with_non_numeric_data():
    array = [
        [1, 'a', 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6]
    ]
    with pytest.raises(ValueError, match="array must be non-empty and all sublists must have a length of 5."):
        task_func(array)