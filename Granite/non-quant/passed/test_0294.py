import pytest
from src_0294 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    ax, combinations, sums = task_func(elements, subset_size)
    assert ax is not None
    assert combinations == [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
    assert sums == [6, 7, 8, 9, 10, 11, 10, 11, 12, 13]