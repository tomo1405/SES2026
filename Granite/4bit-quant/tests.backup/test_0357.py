import pytest
import numpy as np
import matplotlib.pyplot as plt
import cmath
from src_0357 import task_func

def test_task_func():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    ax, Z = task_func(x, y)
    assert isinstance(ax, plt.Axes)
    assert Z.shape == (3, 3)
    assert np.all(Z == 0)

def test_task_func_empty_arrays():
    x = np.array([])
    y = np.array([])
    ax, Z = task_func(x, y)
    assert ax is None
    assert Z.size == 0

def test_task_func_mismatched_sizes():
    x = np.array([1, 2, 3])
    y = np.array([4, 5])
    with pytest.raises(ValueError):
        task_func(x, y)

def test_task_func_non_ndarray():
    x = [1, 2, 3]
    y = np.array([4, 5, 6])
    with pytest.raises(TypeError):
        task_func(x, y)