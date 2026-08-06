import numpy as np
import matplotlib.pyplot as plt
import cmath
from src_0357 import task_func

def test_valid_input():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    ax, Z = task_func(x, y)
    assert isinstance(ax, plt.Axes)
    assert isinstance(Z, np.ndarray)
    assert Z.shape == (len(y), len(x))

def test_empty_input():
    x = np.array([])
    y = np.array([])
    ax, Z = task_func(x, y)
    assert ax is None
    assert isinstance(Z, np.ndarray)
    assert Z.size == 0

def test_mismatched_sizes():
    x = np.array([1, 2, 3])
    y = np.array([4, 5])
    try:
        task_func(x, y)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"