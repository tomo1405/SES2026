import pytest
from src_0294 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    ax, combinations, sums = task_func(elements, subset_size)
    assert ax is not None
    assert combinations is not None
    assert sums is not None
    assert len(combinations) == len(sums)
    assert all(isinstance(sum, int) for sum in sums)
    assert all(sum >= subset_size for sum in sums)
    assert all(sum <= len(elements) for sum in sums)