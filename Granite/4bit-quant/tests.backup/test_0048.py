import pytest
from src_0048 import task_func

def test_task_func():
    df = ... # provide a sample input DataFrame
    expected_df = ... # provide the expected output DataFrame
    expected_heatmap = ... # provide the expected heatmap plot
    df, heatmap = task_func(df)
    assert df.equals(expected_df)
    assert heatmap == expected_heatmap