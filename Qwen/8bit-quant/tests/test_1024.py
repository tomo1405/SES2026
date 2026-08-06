import pytest
from src_1024 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

# Mocking plt.show to prevent actual plotting during tests
plt.show = lambda: None

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty."):
        task_func(df)

def test_task_func_non_numeric_columns():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    })
    with pytest.raises(TypeError, match="All columns must be numeric for correlation calculation."):
        task_func(df)

def test_task_func_single_column():
    df = pd.DataFrame({
        'A': [1, 2, 3]
    })
    with pytest.raises(ValueError, match="DataFrame must have at least two columns for correlation calculation."):
        task_func(df)

def test_task_func_valid_dataframe():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 3, 2, 1],
        'C': [2, 3, 4, 5]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    # Additional checks can be added to verify the plot, such as checking the data points plotted

def test_task_func_identical_columns():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [1, 2, 3, 4]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    # Additional checks can be added to verify the plot, such as checking the data points plotted

def test_task_func_negative_correlation():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [-4, -3, -2, -1]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    # Additional checks can be added to verify the plot, such as checking the data points plotted