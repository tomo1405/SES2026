import pytest
from src_0108 import task_func
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func_empty_df():
    df = pd.DataFrame(columns=['group', 'date', 'value'])
    with pytest.raises(ValueError, match="DataFrame must be non-empty"):
        task_func(df)

def test_task_func_missing_columns():
    df = pd.DataFrame({'group': [1], 'date': ['2023-01-01']})
    with pytest.raises(ValueError, match="DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."):
        task_func(df)

def test_task_func_invalid_date_format():
    df = pd.DataFrame({'group': [1], 'date': ['not-a-date'], 'value': [10]})
    with pytest.raises(ValueError, match="'date' column must be in datetime format."):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    df['date'] = pd.to_datetime(df['date'])
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 1  # Scatter plot collection

def test_task_func_custom_n_clusters():
    df = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    df['date'] = pd.to_datetime(df['date'])
    ax = task_func(df, n_clusters=2)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 1  # Scatter plot collection

def test_task_func_custom_random_state():
    df = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    df['date'] = pd.to_datetime(df['date'])
    ax = task_func(df, random_state=42)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 1  # Scatter plot collection