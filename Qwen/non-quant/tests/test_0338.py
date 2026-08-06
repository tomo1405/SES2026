import pytest
from src_0338 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [10, 20, 30, 40, 50, 60]
    }
    return pd.DataFrame(data)

def test_task_func_output_type(sample_df):
    ax = task_func(sample_df, 'Category', 'Value')
    assert isinstance(ax, plt.Axes)

def test_task_func_bar_count(sample_df):
    ax = task_func(sample_df, 'Category', 'Value')
    bars = ax.patches
    assert len(bars) == 3  # There should be 3 bars for each unique category

def test_task_func_bar_heights(sample_df):
    ax = task_func(sample_df, 'Category', 'Value')
    expected_means = [15, 35, 55]  # Means of values for categories A, B, C
    for i, bar in enumerate(ax.patches):
        assert np.isclose(bar.get_height(), expected_means[i])

def test_task_func_error_bars(sample_df):
    ax = task_func(sample_df, 'Category', 'Value')
    expected_stds = [5, 5, 5]  # Standard deviations of values for categories A, B, C
    for i, bar in enumerate(ax.patches):
        error_bar = bar.errorbarlines[0]
        assert np.isclose(error_bar.get_segments()[0][1][1], expected_stds[i])

def test_task_func_labels(sample_df):
    ax = task_func(sample_df, 'Category', 'Value')
    assert ax.get_xlabel() == 'Category'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Bar chart of Value by Category'

def test_task_func_xticks(sample_df):
    ax = task_func(sample_df, 'Category', 'Value')
    xticklabels = [label.get_text() for label in ax.get_xticklabels()]
    assert xticklabels == ['A', 'B', 'C']

def test_task_func_legend(sample_df):
    ax = task_func(sample_df, 'Category', 'Value')
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == ['Group 1', 'Group 2', 'Group 3']