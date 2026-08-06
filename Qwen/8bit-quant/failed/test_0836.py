import pytest
from src_0836 import task_func

def test_task_func_basic():
    # Test with default parameters
    df = task_func(n_rows=5, remove_cols=[0, 2])
    assert df.shape == (5, 3)  # 5 rows and 3 columns left after removing columns at indices 0 and 2
    assert all(col in df.columns for col in ['B', 'D', 'E'])
    assert all(col not in df.columns for col in ['A', 'C'])

def test_task_func_custom_columns():
    # Test with custom columns
    df = task_func(n_rows=5, remove_cols=[1, 3], columns=['X', 'Y', 'Z', 'W', 'V'])
    assert df.shape == (5, 3)  # 5 rows and 3 columns left after removing columns at indices 1 and 3
    assert all(col in df.columns for col in ['X', 'Z', 'V'])
    assert all(col not in df.columns for col in ['Y', 'W'])

def test_task_func_no_remove():
    # Test with no columns removed
    df = task_func(n_rows=5, remove_cols=[])
    assert df.shape == (5, 5)  # All 5 columns should be present
    assert all(col in df.columns for col in ['A', 'B', 'C', 'D', 'E'])

def test_task_func_all_remove():
    # Test with all columns removed
    df = task_func(n_rows=5, remove_cols=[0, 1, 2, 3, 4])
    assert df.shape == (5, 0)  # No columns left after removing all

def test_task_func_random_seed():
    # Test with random seed to ensure reproducibility
    df1 = task_func(n_rows=5, remove_cols=[0, 2], random_seed=42)
    df2 = task_func(n_rows=5, remove_cols=[0, 2], random_seed=42)
    assert df1.equals(df2)  # Both DataFrames should be identical

def test_task_func_empty_df():
    # Test with 0 rows
    df = task_func(n_rows=0, remove_cols=[0, 2])
    assert df.shape == (0, 3)  # 0 rows and 3 columns left after removing columns at indices 0 and 2

def test_task_func_invalid_remove_cols():
    # Test with invalid remove_cols (out of range)
    with pytest.raises(IndexError):
        task_func(n_rows=5, remove_cols=[5, 6])

def test_task_func_invalid_remove_cols_type():
    # Test with invalid remove_cols type
    with pytest.raises(TypeError):
        task_func(n_rows=5, remove_cols='invalid')