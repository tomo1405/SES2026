import pytest
from src_0951 import task_func
import numpy as np

def test_task_func_default_values():
    U, s, Vh = task_func()
    assert U.shape == (3, 3)
    assert len(s) == 2
    assert Vh.shape == (2, 2)

def test_task_func_custom_dimensions():
    U, s, Vh = task_func(rows=4, columns=3)
    assert U.shape == (4, 4)
    assert len(s) == 3
    assert Vh.shape == (3, 3)

def test_task_func_seed_consistency():
    U1, s1, Vh1 = task_func(seed=0)
    U2, s2, Vh2 = task_func(seed=0)
    assert np.allclose(U1, U2)
    assert np.allclose(s1, s2)
    assert np.allclose(Vh1, Vh2)

def test_task_func_randomness():
    U1, s1, Vh1 = task_func(seed=0)
    U2, s2, Vh2 = task_func(seed=1)
    assert not np.allclose(U1, U2)
    assert not np.allclose(s1, s2)
    assert not np.allclose(Vh1, Vh2)