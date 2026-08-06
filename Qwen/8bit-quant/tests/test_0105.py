import pytest
from src_0105 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_invalid_df():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'group': ['A', 'B'],
        'date': ['2023-01-01', '2023-01-02']
    })
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({
        'group': ['A', 'A', 'B', 'B'],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # Two scatter plots for two groups

def test_task_func_custom_groups():
    df = pd.DataFrame({
        'group': ['X', 'X', 'Y', 'Y'],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    ax = task_func(df, groups=['X', 'Y'])
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # Two scatter plots for two custom groups

def test_task_func_no_matching_groups():
    df = pd.DataFrame({
        'group': ['A', 'A'],
        'date': ['2023-01-01', '2023-01-02'],
        'value': [10, 20]
    })
    ax = task_func(df, groups=['B', 'C'])
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 0  # No scatter plots for non-matching groups