import numpy as np
from scipy.linalg import svd
from src_0951 import task_func
import pytest

def test_task_func_shape():
    U, s, Vh = task_func()
    assert U.shape == (3, 3)
    assert s.shape == (3,)
    assert Vh.shape == (3, 2)

def test_task_func_seed():
    U1, s1, Vh1 = task_func(seed=0)
    U2, s2, Vh2 = task_func(seed=0)
    assert np.array_equal(U1, U2)
    assert np.array_equal(s1, s2)
    assert np.array_equal(Vh1, Vh2)

def test_task_func_rows_columns():
    U1, s1, Vh1 = task_func(rows=3, columns=2)
    U2, s2, Vh2 = task_func(rows=3, columns=2)
    assert np.array_equal(U1, U2)
    assert np.array_equal(s1, s2)
    assert np.array_equal(Vh1, Vh2)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(rows=-1, columns=2)
    with pytest.raises(ValueError):
        task_func(rows=3, columns=-2)
    with pytest.raises(ValueError):
        task_func(rows=-1, columns=-2)