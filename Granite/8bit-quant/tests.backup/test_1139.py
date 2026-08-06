import numpy as np
import itertools
from src_1139 import task_func

def test_task_func():
    matrix = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    sorted_array, combinations = task_func(matrix)
    assert isinstance(sorted_array, np.ndarray)
    assert sorted_array.shape == (9,)
    assert sorted_array.dtype == np.dtype('int64')
    assert isinstance(combinations, list)
    assert len(combinations) == 3 * 2 * 1 / 2
    assert all(isinstance(c, tuple) for c in combinations)
    assert all(len(c) == 2 for c in combinations)
    assert all(a < b for a, b in combinations)