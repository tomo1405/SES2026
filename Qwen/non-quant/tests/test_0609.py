import pytest
from src_0609 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6],
        'D': [6, 5, 4, 3, 2],
        'E': [1, 1, 1, 1, 1]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_tuples():
    return [(1, 5), (2, 4)]

def test_task_func_empty_df():
    df = pd.DataFrame()
    tuples = [(1, 5), (2, 4)]
    n_plots = 2
    result_df, plots = task_func(df, tuples, n_plots)
    assert result_df.empty
    assert not plots

def test_task_func_no_tuples(sample_df):
    tuples = []
    n_plots = 2
    result_df, plots = task_func(sample_df, tuples, n_plots)
    assert result_df.equals(sample_df)
    assert len(plots) == min(n_plots, len(sample_df.columns) // 2)

def test_task_func_with_tuples(sample_df, sample_tuples):
    n_plots = 2
    result_df, plots = task_func(sample_df, sample_tuples, n_plots)
    expected_df = sample_df[~sample_df.apply(tuple, axis=1).isin(sample_tuples)]
    assert result_df.equals(expected_df)
    assert len(plots) == min(n_plots, len(result_df.columns) // 2)

def test_task_func_zero_plots(sample_df, sample_tuples):
    n_plots = 0
    result_df, plots = task_func(sample_df, sample_tuples, n_plots)
    expected_df = sample_df[~sample_df.apply(tuple, axis=1).isin(sample_tuples)]
    assert result_df.equals(expected_df)
    assert not plots

def test_task_func_more_plots_than_columns(sample_df, sample_tuples):
    n_plots = 10
    result_df, plots = task_func(sample_df, sample_tuples, n_plots)
    expected_df = sample_df[~sample_df.apply(tuple, axis=1).isin(sample_tuples)]
    assert result_df.equals(expected_df)
    assert len(plots) == len(expected_df.columns) // 2