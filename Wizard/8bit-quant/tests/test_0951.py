python
import numpy as np
import pytest
from src_0951 import task_func

def test_task_func():
    U, s, Vh = task_func(rows=3, columns=2, seed=0)
    assert U.shape == (3, 3)
    assert s.shape == (2,)
    assert Vh.shape == (2, 2)
    assert np.allclose(np.dot(U * s, Vh), np.eye(3))