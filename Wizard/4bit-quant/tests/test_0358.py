python
import numpy as np
import pytest
from src_0358 import task_func

def test_task_func():
    x = np.linspace(-5, 5, 100)
    complex_dist = task_func(x)
    assert isinstance(complex_dist, np.ndarray)
    assert complex_dist.shape == (100,)
    assert complex_dist.dtype == np.complex128