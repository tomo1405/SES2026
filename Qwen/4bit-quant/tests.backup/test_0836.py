import pytest
from src_0836 import task_func

def test_task_func_basic():
    # Test with default parameters
    df = task_func(5, [1, 3])
    assert df.shape == (5, 3)  # Should have 5 rows and 3 columns (removed columns B and D)
    assert all(col in df.columns for col in ['A', 'C', 'E'])

def test_task_func_with_custom_columns():
    # Test with custom columns
    df = task_func(5, [0, 2], columns=['X', 'Y', 'Z', 'W', 'V'])
    assert df.shape == (5, 3)  # Should have 5 rows and 3 columns (removed columns X and Z)
    assert all(col in df.columns for col in ['Y', 'W', 'V'])

def test_task_func_with_random_seed():
    # Test with random seed for reproducibility
    df1 = task_func(5, [1, 3], random_seed=42)
    df2 = task_func(5, [1, 3], random_seed=42)
    assert df1.equals(df2)  # Both DataFrames should be identical

def test_task_func_no_columns_removed():
    # Test with no columns removed
    df = task_func(5, [])
    assert df.shape == (5, 5)  # Should have 5 rows and 5 columns (no columns removed)
    assert all(col in df.columns for col in ['A', 'B', 'C', 'D', 'E'])

def test_task_func_all_columns_removed():
    # Test with all columns removed
    df = task_func(5, [0, 1, 2, 3, 4])
    assert df.shape == (5, 0)  # Should have 5 rows and 0 columns (all columns removed)
    assert df.empty

def test_task_func_invalid_remove_cols():
    # Test with invalid remove_cols
    with pytest.raises(IndexError):
        task_func(5, [5])  # Column index out of range

def test_task_func_zero_rows():
    # Test with zero rows
    df = task_func(0, [1, 3])
    assert df.shape == (0, 3)  # Should have 0 rows and 3 columns (removed columns B and D)
    assert df.empty