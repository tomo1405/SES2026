import pandas as pd
import pytest
import time

from src_0652 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

def test_task_func(df):
    target_value = '2'
    counts, ax = task_func(df, target_value)
    assert isinstance(counts, pd.Series)
    assert ax is not None or ax is None
    assert 'Operation completed in' in counts.name

def test_task_func_empty_df(df):
    df = pd.DataFrame()
    target_value = '2'
    counts, ax = task_func(df, target_value)
    assert counts is None
    assert ax is None