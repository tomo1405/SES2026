import pytest
from src_0737 import task_func
import numpy as np
from scipy import stats

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = np.hstack(L)
    mode = stats.mode(flattened)[0][0]
    assert task_func(L) == mode

    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    flattened = np.hstack(L)
    mode = stats.mode(flattened)[0][0]
    assert task_func(L) == mode

    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    flattened = np.hstack(L)
    mode = stats.mode(flattened)[0][0]
    assert task_func(L) == mode