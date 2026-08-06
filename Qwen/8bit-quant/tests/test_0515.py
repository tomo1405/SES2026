import pytest
from src_0515 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_array():
    return [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6]
    ]

def test_task_func_output(sample_array):
    df, ax = task_func(sample_array)
    
    # Check DataFrame
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (3, 5)
    
    # Check sums
    expected_sums = pd.Series([8, 9, 10, 11, 12], index=expected_columns)
    assert df.sum().equals(expected_sums)
    
    # Check plot
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 5  # One bar per column

def test_task_func_empty_array():
    empty_array = []
    df, ax = task_func(empty_array)
    
    # Check DataFrame
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns
    assert df.shape == (0, 5)
    
    # Check sums
    expected_sums = pd.Series([0, 0, 0, 0, 0], index=expected_columns)
    assert df.sum().equals(expected_sums)
    
    # Check plot
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0  # No bars for empty data