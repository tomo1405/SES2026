import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0108 import task_func


def test_task_func_invalid_dataframe():
    # Test with an empty DataFrame
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df_empty)

    # Test with missing columns
    df_missing_columns = pd.DataFrame({'group': [1], 'date': ['2023-01-01']})
    with pytest.raises(ValueError):
        task_func(df_missing_columns)

def test_task_func_invalid_date_column():
    # Test with a non-datetime 'date' column
    df_non_datetime = pd.DataFrame({'group': [1], 'date': [1], 'value': [1]})
    with pytest.raises(ValueError):
        task_func(df_non_datetime)

def test_task_func_valid_input():
    # Test with valid input
    df_valid = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    df_valid['date'] = pd.to_datetime(df_valid['date'])
    
    ax = task_func(df_valid, n_clusters=2, random_state=0)
    assert isinstance(ax, plt.Axes)

def test_task_func_kmeans_result():
    # Test the KMeans clustering result
    df_valid = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    df_valid['date'] = pd.to_datetime(df_valid['date'])
    
    ax = task_func(df_valid, n_clusters=2, random_state=0)
    scatter = ax.collections[0]
    points = scatter.get_offsets()
    colors = scatter.get_array()

    assert len(points) == 4
    assert len(colors) == 4
    assert np.all(np.isin(colors, [0, 1]))  # Assuming two clusters labeled 0 and 1

def test_task_func_plot_labels():
    # Test plot labels
    df_valid = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'value': [10, 20, 30, 40]
    })
    df_valid['date'] = pd.to_datetime(df_valid['date'])
    
    ax = task_func(df_valid, n_clusters=2, random_state=0)
    assert ax.get_title() == 'KMeans Clustering of Value vs Date'
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'