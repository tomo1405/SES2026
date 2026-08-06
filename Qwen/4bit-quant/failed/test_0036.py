import pytest
from src_0036 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4],
        'B': [4, 3, 2, 1],
        'C': [2, 2, 2, 2]
    }
    return pd.DataFrame(data)

def test_task_func_with_default_target_values(sample_df):
    result_df, ax = task_func(sample_df)
    assert result_df.equals(pd.DataFrame({
        'A': [1, 0, 3, 4],
        'B': [4, 3, 2, 1],
        'C': [0, 0, 0, 0]
    }))
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_target_values(sample_df):
    result_df, ax = task_func(sample_df, target_values=[2, 3])
    assert result_df.equals(pd.DataFrame({
        'A': [0, 0, 3, 0],
        'B': [0, 3, 0, 0],
        'C': [2, 2, 2, 2]
    }))
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame()
    result_df, ax = task_func(empty_df)
    assert result_df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_all_values_not_in_target(sample_df):
    result_df, ax = task_func(sample_df, target_values=[5, 6])
    assert result_df.equals(pd.DataFrame({
        'A': [0, 0, 0, 0],
        'B': [0, 0, 0, 0],
        'C': [0, 0, 0, 0]
    }))
    assert isinstance(ax, plt.Axes)

def test_task_func_single_column(sample_df):
    single_column_df = sample_df[['A']]
    result_df, ax = task_func(single_column_df)
    assert result_df.equals(pd.DataFrame({
        'A': [1, 0, 3, 4]
    }))
    assert isinstance(ax, plt.Axes)