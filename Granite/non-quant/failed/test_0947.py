import pytest
from src_0947 import task_func

def test_task_func():
    # Test case 1: Default arguments
    df = task_func()
    assert df.shape == (3, 2)
    assert df.min().item() == 0
    assert df.max().item() == 100

    # Test case 2: Custom arguments
    df = task_func(rows=5, cols=4, min_val=1, max_val=10, seed=123)
    assert df.shape == (5, 4)
    assert df.min().item() == 1
    assert df.max().item() == 10