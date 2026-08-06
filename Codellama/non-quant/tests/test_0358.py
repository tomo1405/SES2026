import pytest
from src_0358 import task_func
import numpy as np

def test_task_func():
    x = np.array([1, 2, 3, 4, 5])
    complex_dist = task_func(x)
    assert isinstance(complex_dist, np.ndarray)
    assert complex_dist.shape == (5,)
    assert np.allclose(complex_dist.real, np.array([0.39894228, 0.39894228, 0.39894228, 0.39894228, 0.39894228]))
    assert np.allclose(complex_dist.imag, np.array([0.39894228, 0.39894228, 0.39894228, 0.39894228, 0.39894228]))