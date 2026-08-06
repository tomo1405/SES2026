import pandas as pd
import pytest
from src_0142 import task_func


def test_task_func_with_default_parameters():
    rows = 5
    df, stats_dict = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, 6)
    assert isinstance(stats_dict, dict)
    assert all(col in stats_dict for col in ['A', 'B', 'C', 'D', 'E', 'F'])
    for col in ['A', 'B', 'C', 'D', 'E', 'F']:
        assert 'mean' in stats_dict[col]
        assert 'median' in stats_dict[col]

def test_task_func_with_custom_columns():
    rows = 3
    columns = ['X', 'Y']
    df, stats_dict = task_func(rows, columns=columns)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, len(columns))
    assert isinstance(stats_dict, dict)
    assert all(col in stats_dict for col in columns)
    for col in columns:
        assert 'mean' in stats_dict[col]
        assert 'median' in stats_dict[col]

def test_task_func_with_invalid_rows():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_with_zero_rows():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_with_non_integer_rows():
    with pytest.raises(ValueError):
        task_func('a')

def test_task_func_with_seed():
    rows = 5
    df1, _ = task_func(rows, seed=42)
    df2, _ = task_func(rows, seed=42)
    assert df1.equals(df2)

def test_task_func_with_different_seed():
    rows = 5
    df1, _ = task_func(rows, seed=42)
    df2, _ = task_func(rows, seed=99)
    assert not df1.equals(df2)