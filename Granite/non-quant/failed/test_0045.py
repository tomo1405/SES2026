import pytest
from src_0045 import task_func

def test_task_func():
    df = # create or provide a sample input DataFrame
    expected_df = # create or provide the expected output DataFrame
    expected_ax = # create or provide the expected output axis object
    df_output, ax_output = task_func(df)
    assert df_output.equals(expected_df)
    assert ax_output == expected_ax