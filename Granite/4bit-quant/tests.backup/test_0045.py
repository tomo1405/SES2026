import pytest
from src_0045 import task_func

def test_task_func():
    df = # create or load a sample dataframe for testing
    expected_df = # expected output dataframe after applying the function
    expected_ax = # expected output axis object after applying the function
    df_output, ax_output = task_func(df)
    assert df_output.equals(expected_df)
    assert ax_output == expected_ax