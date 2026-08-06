import pytest
from src_0951 import task_func
import numpy as np
from scipy.linalg import svd

def test_task_func_default():
    U, s, Vh = task_func()
    assert U.shape == (3, 3)
    assert s.shape == (2,)
    assert Vh.shape == (2, 2)

def test_task_func_custom_dimensions():
    U, s, Vh = task_func(rows=4, columns=3)
    assert U.shape == (4, 4)
    assert s.shape == (3,)
    assert Vh.shape == (3, 3)

def test_task_func_seed_consistency():
    U1, s1, Vh1 = task_func(seed=42)
    U2, s2, Vh2 = task_func(seed=42)
    np.testing.assert_array_equal(U1, U2)
    np.testing.assert_array_equal(s1, s2)
    np.testing.assert_array_equal(Vh1, Vh2)

def test_task_func_negative_rows():
    with pytest.raises(ValueError):
        task_func(rows=-1)

def test_task_func_negative_columns():
    with pytest.raises(ValueError):
        task_func(columns=-1)

def test_task_func_zero_rows():
    with pytest.raises(ValueError):
        task_func(rows=0)

def test_task_func_zero_columns():
    with pytest.raises(ValueError):
        task_func(columns=0)