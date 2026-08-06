import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0342 import task_func


def test_task_func_with_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, 'column_name')

def test_task_func_with_non_existent_column():
    df = pd.DataFrame({'column1': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, 'non_existent_column')

def test_task_func_with_numeric_column():
    df = pd.DataFrame({'column1': [1, 2, 3, 4, 5]})
    fig = task_func(df, 'column1')
    assert isinstance(fig, plt.Figure)

def test_task_func_with_categorical_column():
    df = pd.DataFrame({'column1': ['A', 'B', 'A', 'C', 'B']})
    fig = task_func(df, 'column1')
    assert isinstance(fig, plt.Figure)

def test_task_func_with_mixed_data_types():
    df = pd.DataFrame({'column1': [1, 2, 3, 'A', 'B']})
    with pytest.raises(ValueError):
        task_func(df, 'column1')

def test_task_func_with_large_dataframe():
    df = pd.DataFrame({'column1': np.random.randint(0, 100, size=1000)})
    fig = task_func(df, 'column1')
    assert isinstance(fig, plt.Figure)