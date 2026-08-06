import pandas as pd
import pytest
from src_0142 import task_func


def test_task_func_positive_rows():
    rows = 10
    columns = ['A', 'B', 'C', 'D', 'E', 'F']
    seed = 42
    df, stats_dict = task_func(rows, columns, seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    assert len(stats_dict) == len(columns)
    for col in columns:
        assert col in stats_dict
        assert isinstance(stats_dict[col], dict)
        assert 'mean' in stats_dict[col]
        assert 'median' in stats_dict[col]

def test_task_func_negative_rows():
    rows = -1
    columns = ['A', 'B', 'C', 'D', 'E', 'F']
    seed = 42
    with pytest.raises(ValueError):
        task_func(rows, columns, seed)

def test_task_func_invalid_columns():
    rows = 10
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    seed = 42
    with pytest.raises(ValueError):
        task_func(rows, columns, seed)

def test_task_func_invalid_seed():
    rows = 10
    columns = ['A', 'B', 'C', 'D', 'E', 'F']
    seed = 'abc'
    with pytest.raises(ValueError):
        task_func(rows, columns, seed)