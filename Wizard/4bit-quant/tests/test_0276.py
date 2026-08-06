python
import numpy as np
from itertools import combinations
import pytest

def task_func(n):

    if n < 1:
        raise ValueError("Input must be a positive integer")
    numbers = np.arange(1, n + 1)
    pairs = list(combinations(numbers, 2))
    return pairs

def test_task_func():
    with pytest.raises(ValueError):
        task_func(-1)
    assert task_func(1) == [(1, 1)]
    assert task_func(2) == [(1, 2), (2, 1)]
    assert task_func(3) == [(1, 2), (1, 3), (2, 3)]
    assert task_func(4) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]