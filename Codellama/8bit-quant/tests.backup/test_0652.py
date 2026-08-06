import pytest
from src_0652 import task_func
import pandas as pd

def test_task_func():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    target_value = "target"
    counts, ax = task_func(df, target_value)
    assert counts.empty
    assert ax is None

    # Test case 2: Non-empty DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    target_value = "target"
    counts, ax = task_func(df, target_value)
    assert not counts.empty
    assert ax is not None
    assert ax.get_title() == "Counts"
    assert ax.get_xlabel() == "Column"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["A", "B"]
    assert ax.get_yticklabels() == [0, 1, 2]

    # Test case 3: Target value not in DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    target_value = "target"
    counts, ax = task_func(df, target_value)
    assert counts.empty
    assert ax is None

    # Test case 4: Target value in DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    target_value = 4
    counts, ax = task_func(df, target_value)
    assert not counts.empty
    assert ax is not None
    assert ax.get_title() == "Counts"
    assert ax.get_xlabel() == "Column"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["A", "B"]
    assert ax.get_yticklabels() == [0, 1, 2]

    # Test case 5: DataFrame with multiple columns
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    target_value = 4
    counts, ax = task_func(df, target_value)
    assert not counts.empty
    assert ax is not None
    assert ax.get_title() == "Counts"
    assert ax.get_xlabel() == "Column"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["A", "B", "C"]
    assert ax.get_yticklabels() == [0, 1, 2]