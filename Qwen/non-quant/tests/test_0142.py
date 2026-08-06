import pandas as pd
import pytest
from src_0142 import task_func


def test_task_func_valid_input():
    rows = 5
    df, stats_dict = task_func(rows)
    
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, 6)
    assert all(col in df.columns for col in ['A', 'B', 'C', 'D', 'E', 'F'])
    
    for col in ['A', 'B', 'C', 'D', 'E', 'F']:
        assert isinstance(stats_dict[col]['mean'], float)
        assert isinstance(stats_dict[col]['median'], float)

def test_task_func_invalid_rows():
    with pytest.raises(ValueError, match="rows must be a positive integer greater than 0."):
        task_func(0)

def test_task_func_non_integer_rows():
    with pytest.raises(ValueError, match="rows must be a positive integer greater than 0."):
        task_func('five')

def test_task_func_negative_rows():
    with pytest.raises(ValueError, match="rows must be a positive integer greater than 0."):
        task_func(-3)

def test_task_func_custom_columns():
    rows = 3
    columns = ['X', 'Y']
    df, stats_dict = task_func(rows, columns=columns)
    
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, 2)
    assert all(col in df.columns for col in columns)
    
    for col in columns:
        assert isinstance(stats_dict[col]['mean'], float)
        assert isinstance(stats_dict[col]['median'], float)

def test_task_func_seed_consistency():
    rows = 4
    columns = ['P', 'Q', 'R']
    df1, _ = task_func(rows, columns=columns, seed=42)
    df2, _ = task_func(rows, columns=columns, seed=42)
    
    assert df1.equals(df2)