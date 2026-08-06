import pytest
from src_0176 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_empty_df():
    df = pd.DataFrame()
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_missing_columns():
    df = pd.DataFrame({'Likes': [10], 'Views': [20]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_interesting_videos():
    df = pd.DataFrame({
        'Title': ['Not Interesting', 'Another Boring Title'],
        'Likes': [10, 20],
        'Views': [100, 200]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_interesting_videos():
    df = pd.DataFrame({
        'Title': ['How to Code', 'What is Python', 'Unrelated Video'],
        'Likes': [10, 20, 5],
        'Views': [100, 200, 1000]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert 'Like Ratio' in ax.get_legend_handles_labels()[1]
    assert ax.get_ylabel() == 'Like Ratio'
    assert all(label.get_rotation() == 'vertical' for label in ax.get_xticklabels())

def test_task_func_with_zero_views():
    df = pd.DataFrame({
        'Title': ['How to Code', 'What is Python'],
        'Likes': [10, 20],
        'Views': [0, 0]
    })
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert 'Like Ratio' in ax.get_legend_handles_labels()[1]
    assert ax.get_ylabel() == 'Like Ratio'
    assert all(label.get_rotation() == 'vertical' for label in ax.get_xticklabels())