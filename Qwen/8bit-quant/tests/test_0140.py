import pytest
from src_0140 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': ['a', 'b', 'c', 'd', 'e']
    }
    return pd.DataFrame(data)

def test_task_func_non_dataframe_input():
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func([1, 2, 3])

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func(empty_df)

def test_task_func_no_numeric_columns():
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']})
    with pytest.raises(ValueError, match="DataFrame contains no numeric columns."):
        task_func(df)

def test_task_func_with_numeric_columns(sample_df):
    axes = task_func(sample_df)
    assert len(axes) == 2
    assert isinstance(axes[0], plt.Axes)
    assert isinstance(axes[1], plt.Axes)

@patch('matplotlib.pyplot.subplots')
def test_task_func_plotting(mock_subplots, sample_df):
    task_func(sample_df)
    mock_subplots.assert_called_with()

@patch('matplotlib.pyplot.subplots')
def test_task_func_plot_titles(mock_subplots, sample_df):
    task_func(sample_df)
    calls = [call[1]['title'] for call in mock_subplots.call_args_list]
    assert calls == ['A', 'B']

@patch('matplotlib.pyplot.subplots')
def test_task_func_axis_labels(mock_subplots, sample_df):
    task_func(sample_df)
    for call in mock_subplots.call_args_list:
        ax = call[0][1]
        assert ax.get_xlabel() == 'Value'
        assert ax.get_ylabel() == 'Frequency'