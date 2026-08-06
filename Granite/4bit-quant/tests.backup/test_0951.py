import pytest
import numpy as np
from scipy.linalg import svd

def task_func(rows=3, columns=2, seed=0):
    np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    U, s, Vh = svd(matrix)

    return U, s, Vh

class TestTaskFunc:
    def test_task_func_with_default_args(self):
        U, s, Vh = task_func()
        assert U.shape == (3, 3)
        assert s.shape == (3,)
        assert Vh.shape == (2, 2)

    def test_task_func_with_custom_args(self):
        U, s, Vh = task_func(rows=5, columns=4, seed=42)
        assert U.shape == (5, 5)
        assert s.shape == (5,)
        assert Vh.shape == (4, 4)

    def test_task_func_with_invalid_args(self):
        with pytest.raises(ValueError):
            task_func(rows=-1, columns=2, seed=0)
        with pytest.raises(ValueError):
            task_func(rows=3, columns=-2, seed=0)
        with pytest.raises(ValueError):
            task_func(rows=3, columns=2, seed=-1)