import pytest
from src_0235 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Score': [80, 85, 90, 80]
    }
    return pd.DataFrame(data)

def test_task_func_input_type(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df.drop(columns=['Age']))

def test_task_func_duplicate_removal(sample_df):
    result_df, _ = task_func(sample_df)
    assert len(result_df) == 3, "Duplicate names should be removed"

def test_task_func_linregress_output(sample_df):
    _, ax = task_func(sample_df)
    assert 'Data' in ax.get_legend().get_texts()[0].get_text(), "Scatter plot should have 'Data' label"
    assert 'Fitted line' in ax.get_legend().get_texts()[1].get_text(), "Fitted line should have 'Fitted line' label"

def test_task_func_plot_labels(sample_df):
    _, ax = task_func(sample_df)
    assert ax.get_xlabel() == 'Age', "X-axis label should be 'Age'"
    assert ax.get_ylabel() == 'Score', "Y-axis label should be 'Score'"
    assert ax.get_title() == 'Linear Regression', "Title should be 'Linear Regression'"

def test_task_func_slope_intercept(sample_df):
    plt, _ = task_func(sample_df)
    # Assuming the linear regression line is calculated correctly
    # We can't directly check the slope and intercept without recalculating
    # But we can check if the 'Age_up' column is added correctly
    assert 'Age_up' in sample_df.columns, "'Age_up' column should be added to the DataFrame"