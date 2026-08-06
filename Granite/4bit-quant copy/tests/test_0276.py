import pytest
from src_0276 import task_func
import numpy as np
from itertools import combinations

def test_task_func():
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func(-1)
    assert task_func(1) == []
    assert task_func(2) == [(1, 2)]
    numbers = np.arange(1, 100 + 1)
    pairs = list(combinations(numbers, 2))
    assert task_func(100) == pairs