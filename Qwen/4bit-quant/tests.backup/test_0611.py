import pytest
from src_0611 import task_func
import pandas as pd

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

def test_task_func_empty_tuples(sample_df):
    df, plots = task_func(sample_df, [], 2)
    assert df.equals(sample_df)
    assert len(plots) == 2

def test_task_func_non_empty_tuples(sample_df):
    df, plots = task_func(sample_df, [(1, 2, 3, 4, 5)], 2)
    assert df.equals(sample_df)
    assert len(plots) == 2

def test_task_func_no_plots(sample_df):
    df, plots = task_func(sample_df, [(1, 2, 3, 4, 5)], 0)
    assert df.equals(sample_df)
    assert len(plots) == 0

def test_task_func_all_rows_dropped(sample_df):
    df, plots = task_func(sample_df, [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8)], 2)
    assert df.empty
    assert len(plots) == 0

def test_task_func_invalid_tuples(sample_df):
    with pytest.raises(KeyError):
        task_func(sample_df, [(1, 2, 3, 4, 25)], 2)