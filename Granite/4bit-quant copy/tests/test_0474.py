import pytest
from src_0474 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    n_walks = 3
    n_steps = 10
    ax = task_func(n_walks, n_steps)
    assert ax is not None
    # Test case 2: Test with invalid input
    with pytest.raises(ValueError):
        task_func(-1, 10)
    with pytest.raises(ValueError):
        task_func(10, -1)