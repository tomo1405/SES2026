import pytest
from src_0949 import task_func

def test_task_func():
    # Test case 1: Default input values
    scaled_matrix = task_func()
    assert scaled_matrix.shape == (3, 2)
    assert scaled_matrix.min() >= 0
    assert scaled_matrix.max() <= 1

    # Test case 2: Custom input values
    scaled_matrix = task_func(rows=5, columns=4, seed=123)
    assert scaled_matrix.shape == (5, 4)
    assert scaled_matrix.min() >= 0
    assert scaled_matrix.max() <= 1