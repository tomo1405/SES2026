import pytest
from src_1024 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import sys

# Mocking plt.show() to capture output
class MockDisplay:
    def __init__(self):
        self.display_list = []

    def __call__(self, *args, **kwargs):
        self.display_list.append((args, kwargs))

@pytest.fixture
def mock_display(monkeypatch):
    display = MockDisplay()
    monkeypatch.setattr(plt, 'show', display)
    return display

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty."):
        task_func(df)

def test_task_func_non_numeric_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    with pytest.raises(TypeError, match="All columns must be numeric for correlation calculation."):
        task_func(df)

def test_task_func_single_column():
    df = pd.DataFrame({'A': [1, 2, 3]})
    with pytest.raises(ValueError, match="DataFrame must have at least two columns for correlation calculation."):
        task_func(df)

def test_task_func_valid_data(mock_display):
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [2, 3, 4, 5],
        'C': [3, 4, 5, 6]
    })
    ax = task_func(df)
    
    # Check that plt.show was called
    assert len(mock_display.display_list) == 1
    
    # Check that the returned Axes object is not None
    assert ax is not None

def test_task_func_highest_correlation():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [2, 3, 4, 5],
        'C': [3, 4, 5, 6]
    })
    ax = task_func(df)
    
    # Check that the highest correlation is between 'A' and 'B'
    corr_matrix = df.corr()
    abs_corr_matrix = corr_matrix.abs()
    highest_corr_value = abs_corr_matrix.unstack().dropna().nlargest(2).iloc[-1]
    max_corr_pair = np.where(abs_corr_matrix == highest_corr_value)
    column_x = df.columns[max_corr_pair[0][0]]
    column_y = df.columns[max_corr_pair[1][0]]
    
    assert column_x == 'A' and column_y == 'B'

def test_task_func_plot_title_and_labels(mock_display):
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [2, 3, 4, 5]
    })
    task_func(df)
    
    # Check that the plot title and labels are correct
    fig = plt.gcf()
    assert fig.axes[0].get_title() == "Scatter plot between A and B"
    assert fig.axes[0].get_xlabel() == "A"
    assert fig.axes[0].get_ylabel() == "B"