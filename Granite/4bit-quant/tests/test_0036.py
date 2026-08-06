import pytest
from src_0036 import task_func

def test_task_func():
    df = ... # provide a sample input dataframe
    target_values = [1, 3, 4]
    expected_df = ... # provide the expected output dataframe
    expected_ax = ... # provide the expected output axis object
    df, ax = task_func(df, target_values)
    assert df.equals(expected_df)
    assert ax == expected_ax