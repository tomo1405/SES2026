import pytest
from src_0836 import task_func

def test_task_func():
    # Test case 1: Default arguments
    df = task_func(n_rows=10, remove_cols=[0, 2])
    assert df.shape == (10, 3)
    assert list(df.columns) == ['A', 'B', 'D']

    # Test case 2: Custom arguments
    df = task_func(n_rows=5, remove_cols=[1, 3], columns=['X', 'Y', 'Z'], random_seed=42)
    assert df.shape == (5, 2)
    assert list(df.columns) == ['X', 'Y']

    # Test case 3: edge case
    with pytest.raises(ValueError):
        task_func(n_rows=10, remove_cols=[])