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
    # Test case 1: n = 5
    n = 5
    expected_pairs = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    assert task_func(n) == expected_pairs

    # Test case 2: n = 0
    n = 0
    with pytest.raises(ValueError):
        task_func(n)

    # Test case 3: n = -1
    n = -1
    with pytest.raises(ValueError):
        task_func(n)