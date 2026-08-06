import pytest
from src_0294 import task_func
import itertools
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    ax, combinations, sums = task_func(elements, subset_size)
    assert isinstance(ax, plt.Axes)
    assert isinstance(combinations, list)
    assert isinstance(sums, list)
    assert all(isinstance(c, tuple) for c in combinations)
    assert all(isinstance(s, int) for s in sums)
    assert len(combinations) == len(sums)
    assert all(sum(c) in sums for c in combinations)
    assert ax.patches[0].get_height() == len(combinations)
    assert ax.patches[0].get_x() == min(sums)
    assert ax.patches[-1].get_x() == max(sums)

def test_task_func_invalid_input():
    elements = [1, 2, 3, 4, 5]
    subset_size = 10
    with pytest.raises(ValueError):
        task_func(elements, subset_size)