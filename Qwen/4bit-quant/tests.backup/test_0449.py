import pytest
from src_0449 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_default():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    x, y = ax.lines[0].get_data()
    assert len(x) == 100
    assert len(y) == 100
    assert np.isclose(x[0], -3)
    assert np.isclose(x[-1], 3)
    assert np.allclose(y, norm.pdf(x))

def test_task_func_custom_parameters():
    ax = task_func(mu=5, sigma=2)
    assert isinstance(ax, plt.Axes)
    x, y = ax.lines[0].get_data()
    assert len(x) == 100
    assert len(y) == 100
    assert np.isclose(x[0], 5 - 3 * 2)
    assert np.isclose(x[-1], 5 + 3 * 2)
    assert np.allclose(y, norm.pdf(x, 5, 2))