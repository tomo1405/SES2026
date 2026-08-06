import pytest
from src_0108 import task_func
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_invalid_columns():
    df = pd.DataFrame({'group': [1, 2, 3], 'date': [1, 2, 3], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_invalid_date_format():
    df = pd.DataFrame({'group': [1, 2, 3], 'date': ['a', 'b', 'c'], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({'group': [1, 2, 3], 'date': [1, 2, 3], 'value': [1, 2, 3]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'KMeans Clustering of Value vs Date'
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'