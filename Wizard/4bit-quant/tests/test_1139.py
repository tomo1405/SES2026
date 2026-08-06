python
import itertools
import numpy as np
import pytest

from src_1139 import task_func

def test_task_func():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sorted_array, combinations = task_func(matrix)
    
    assert isinstance(sorted_array, np.ndarray)
    assert isinstance(combinations, list)
    assert len(combinations) == 3
    assert all(isinstance(c, tuple) for c in combinations)
    assert all(len(c) == 2 for c in combinations)
    assert all(isinstance(c[0], int) and isinstance(c[1], int) for c in combinations)
    assert all(c[0] != c[1] for c in combinations)
    assert all(c[0] < c[1] for c in combinations)
    assert all(c[0] < sorted_array.shape[0] and c[1] < sorted_array.shape[0] for c in combinations)