import pytest
from src_0609 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12],
        'D': [13, 14, 15, 16],
        'E': [17, 18, 19, 20]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_tuples():
    return [(1, 5), (3, 11)]

def test_task_func_empty_df(sample_df, sample_tuples):
    df, plots = task_func(pd.DataFrame(), sample_tuples, 2)
    assert df.empty
    assert plots == []

def test_task_func_no_tuples(sample_df, sample_tuples):
    df, plots = task_func(sample_df, [], 2)
    assert df.equals(sample_df)
    assert len(plots) == 2

def test_task_func_with_tuples(sample_df, sample_tuples):
    df, plots = task_func(sample_df, sample_tuples, 2)
    expected_data = {
        'A': [2, 4],
        'B': [6, 8],
        'C': [10, 12],
        'D': [14, 16],
        'E': [18, 20]
    }
    expected_df = pd.DataFrame(expected_data)
    assert df.equals(expected_df)
    assert len(plots) == 2

def test_task_func_no_plots(sample_df, sample_tuples):
    df, plots = task_func(sample_df, sample_tuples, 0)
    assert df.equals(sample_df)
    assert plots == []

def test_task_func_insufficient_columns(sample_df, sample_tuples):
    df_reduced = sample_df.drop(columns=['C', 'D', 'E'])
    df, plots = task_func(df_reduced, sample_tuples, 2)
    assert df.equals(df_reduced)
    assert plots == []

def test_task_func_more_plots_than_available(sample_df, sample_tuples):
    df, plots = task_func(sample_df, sample_tuples, 10)
    assert df.equals(sample_df)
    assert len(plots) == len(COLUMNS) // 2