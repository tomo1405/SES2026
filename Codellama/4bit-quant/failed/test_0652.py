import pytest
from src_0652 import task_func
import pandas as pd

def test_task_func():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    target_value = "target"
    expected_counts = pd.Series([], dtype="int64")
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax

    # Test case 2: Non-empty DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    target_value = "target"
    expected_counts = pd.Series([0, 0, 0], dtype="int64")
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax

    # Test case 3: Non-empty DataFrame with target value
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    target_value = 2
    expected_counts = pd.Series([0, 1, 0], dtype="int64")
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax