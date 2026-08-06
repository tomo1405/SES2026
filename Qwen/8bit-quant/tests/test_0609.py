import pytest
from src_0609 import task_func
import pandas as pd
import seaborn as sns

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
    return [(1, 5), (2, 6)]

def test_task_func_empty_df():
    df = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E'])
    tuples = []
    n_plots = 2
    result_df, plots = task_func(df, tuples, n_plots)
    assert result_df.empty
    assert plots == []

def test_task_func_no_rows_removed(sample_df, sample_tuples):
    n_plots = 2
    result_df, plots = task_func(sample_df, sample_tuples, n_plots)
    assert result_df.equals(sample_df)
    assert len(plots) == min(n_plots, len(sample_df.columns) // 2)

def test_task_func_rows_removed(sample_df, sample_tuples):
    sample_df.loc[0, 'A'] = 1
    sample_df.loc[0, 'B'] = 5
    n_plots = 2
    result_df, plots = task_func(sample_df, sample_tuples, n_plots)
    assert result_df.equals(sample_df.iloc[1:])
    assert len(plots) == min(n_plots, len(result_df.columns) // 2)

def test_task_func_zero_plots(sample_df, sample_tuples):
    n_plots = 0
    result_df, plots = task_func(sample_df, sample_tuples, n_plots)
    assert result_df.equals(sample_df)
    assert plots == []

def test_task_func_more_plots_than_possible(sample_df, sample_tuples):
    n_plots = 10
    result_df, plots = task_func(sample_df, sample_tuples, n_plots)
    assert result_df.equals(sample_df)
    assert len(plots) == len(sample_df.columns) // 2