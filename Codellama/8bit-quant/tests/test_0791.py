import pandas as pd
import pytest
from src_0791 import task_func


def test_task_func():
    # Test case 1: Ensure provided columns exist in the dataframe
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df, "col3", "col4")

    # Test case 2: Ensure scaler is applied correctly
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    task_func(df, "col1", "col2")
    assert df["col1"].equals(pd.Series([-1, 0, 1]))
    assert df["col2"].equals(pd.Series([-1, 0, 1]))

    # Test case 3: Ensure largest_diff_indices is correct
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    largest_diff_indices = task_func(df, "col1", "col2", N=2)
    assert largest_diff_indices == [0, 1]