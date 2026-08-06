import numpy as np
from scipy.linalg import svd
def task_func(rows=3, columns=2, seed=0):
    np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    U, s, Vh = svd(matrix)

    return U, s, Vh
import pytest

def test_task_func():
    # Test case 1: Default input values
    U, s, Vh = task_func()
    assert U.shape == (3, 3)
    assert s.shape == (3,)
    assert Vh.shape == (3, 2)

    # Test case 2: Custom input values
    U, s, Vh = task_func(rows=5, columns=4, seed=42)
    assert U.shape == (5, 5)
    assert s.shape == (5,)
    assert Vh.shape == (5, 4)

    # Test case 3: Invalid input values
    with pytest.raises(ValueError):
        U, s, Vh = task_func(rows=-1, columns=2, seed=0)
    with pytest.raises(ValueError):
        U, s, Vh = task_func(rows=3, columns=-1, seed=0)
    with pytest.raises(ValueError):
        U, s, Vh = task_func(rows=3, columns=2, seed=-1)