import pytest
from src_0048 import task_func

def test_task_func():
    df = # create or load a sample dataframe for testing
    expected_df = # create or load the expected output dataframe after filling missing values and scaling the data
    expected_heatmap = # create or load the expected heatmap plot
    df_output, heatmap_output = task_func(df)
    assert df_output.equals(expected_df)
    assert heatmap_output == expected_heatmap