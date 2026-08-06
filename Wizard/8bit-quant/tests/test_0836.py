python
import pytest
from src_0836 import task_func

def test_task_func():
    # Test case 1: n_rows=10, remove_cols=[0, 1, 2], random_seed=None
    df = task_func(10, [0, 1, 2])
    assert df.shape == (10, 2)
    assert list(df.columns) == ['C', 'D']

    # Test case 2: n_rows=100, remove_cols=[0, 1, 2, 3, 4], random_seed=123
    df = task_func(100, [0, 1, 2, 3, 4], random_seed=123)
    assert df.shape == (100, 0)

    # Test case 3: n_rows=1000, remove_cols=[0, 1, 2, 3, 4], random_seed=456
    df = task_func(1000, [0, 1, 2, 3, 4], random_seed=456)
    assert df.shape == (1000, 0)