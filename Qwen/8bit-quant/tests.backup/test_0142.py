import pytest
from src_0142 import task_func

def test_task_func_invalid_rows():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_zero_rows():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_non_integer_rows():
    with pytest.raises(ValueError):
        task_func('a')

def test_task_func_default_columns():
    df, stats_dict = task_func(5)
    assert df.shape == (5, 6)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E', 'F']
    assert all(isinstance(stats_dict[col]['mean'], float) for col in df.columns)
    assert all(isinstance(stats_dict[col]['median'], float) for col in df.columns)

def test_task_func_custom_columns():
    columns = ['X', 'Y', 'Z']
    df, stats_dict = task_func(3, columns=columns)
    assert df.shape == (3, 3)
    assert list(df.columns) == columns
    assert all(isinstance(stats_dict[col]['mean'], float) for col in df.columns)
    assert all(isinstance(stats_dict[col]['median'], float) for col in df.columns)

def test_task_func_seed_consistency():
    df1, stats_dict1 = task_func(5, seed=42)
    df2, stats_dict2 = task_func(5, seed=42)
    assert df1.equals(df2)
    assert stats_dict1 == stats_dict2

def test_task_func_different_seeds():
    df1, stats_dict1 = task_func(5, seed=42)
    df2, stats_dict2 = task_func(5, seed=123)
    assert not df1.equals(df2)
    assert stats_dict1 != stats_dict2