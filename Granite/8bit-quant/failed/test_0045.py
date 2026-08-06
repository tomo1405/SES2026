import pytest
from src_0045 import task_func

def test_task_func():
    df = # create a sample dataframe for testing
    expected_df = # create the expected dataframe after filling missing values and scaling
    expected_ax = # create the expected axis object for the plot
    df_ returned, ax_returned = task_func(df)
    assert df_returned.equals(expected_df)
    assert ax_returned == expected_ax

def test_task_func_with_missing_values():
    df = # create a sample dataframe with missing values for testing
    expected_df = # create the expected dataframe after filling missing values and scaling
    expected_ax = # create the expected axis object for the plot
    df_returned, ax_returned = task_func(df)
    assert df_returned.equals(expected_df)
    assert ax_returned == expected_ax

def test_task_func_with_zero_std_dev():
    df = # create a sample dataframe with zero standard deviation for testing
    expected_df = # create the expected dataframe after filling missing values and scaling
    expected_ax = # create the expected axis object for the plot
    df_returned, ax_returned = task_func(df)
    assert df_returned.equals(expected_df)
    assert ax_returned == expected_ax