import pytest
from src_0611 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500],
        'D': [1000, 2000, 3000, 4000, 5000],
        'E': [10000, 20000, 30000, 40000, 50000]
    }
    return pd.DataFrame(data)

def test_task_func_no_rows_dropped(sample_df):
    tuples = [(1, 2, 3, 4, 5)]
    df, plots = task_func(sample_df.copy(), tuples, 2)
    assert df.empty
    assert len(plots) == 0

def test_task_func_rows_dropped(sample_df):
    tuples = [(1, 2, 3, 4, 5)]
    df, plots = task_func(sample_df.copy(), tuples, 2)
    assert df.empty
    assert len(plots) == 0

def test_task_func_some_rows_dropped(sample_df):
    tuples = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6)]
    df, plots = task_func(sample_df.copy(), tuples, 2)
    assert not df.empty
    assert len(plots) == 2

def test_task_func_no_plots(sample_df):
    tuples = [(1, 2, 3, 4, 5)]
    df, plots = task_func(sample_df.copy(), tuples, 0)
    assert df.empty
    assert len(plots) == 0

def test_task_func_with_plots(sample_df):
    tuples = []
    df, plots = task_func(sample_df.copy(), tuples, 2)
    assert not df.empty
    assert len(plots) == 2