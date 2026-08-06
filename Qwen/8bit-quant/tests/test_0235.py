import numpy as np
import pandas as pd
import pytest
from src_0235 import task_func


@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Score': [85, 90, 95, 85]
    }
    return pd.DataFrame(data)

def test_task_func_input_type(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df.to_dict())

def test_task_func_drop_duplicates(sample_df):
    result_df, _ = task_func(sample_df)
    assert len(result_df) == 3, "Duplicate names should be dropped"

def test_task_func_linear_regression(sample_df):
    result_df, _ = task_func(sample_df)
    slope, intercept, r_value, _, _ = stats.linregress(result_df['Age'], result_df['Score'])
    assert not np.isnan(slope), "Slope should not be NaN"
    assert not np.isnan(intercept), "Intercept should not be NaN"
    assert not np.isnan(r_value), "R-value should not be NaN"

def test_task_func_plot(sample_df):
    plt, ax = task_func(sample_df)
    assert isinstance(plt, plt.Figure), "Return value should be a matplotlib Figure"
    assert isinstance(ax, plt.Axes), "Return value should be a matplotlib Axes"
    assert 'Age' in ax.get_xlabel(), "X-axis label should be 'Age'"
    assert 'Score' in ax.get_ylabel(), "Y-axis label should be 'Score'"
    assert 'Linear Regression' in ax.get_title(), "Plot title should be 'Linear Regression'"
    assert 'Data' in ax.get_legend_handles_labels()[1], "Legend should include 'Data'"
    assert 'Fitted line' in ax.get_legend_handles_labels()[1], "Legend should include 'Fitted line'"