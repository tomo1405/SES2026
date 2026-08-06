import pytest
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from src_0370 import task_func

def test_task_func():
    # Test with a list of numbers
    l = np.random.rand(100)
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)

    # Test with a list of integers
    l = np.random.randint(0, 100, size=100)
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)

    # Test with an empty list
    l = []
    with pytest.raises(ValueError):
        ax = task_func(l)

    # Test with a list of strings
    l = ['a', 'b', 'c', 'd']
    with pytest.raises(TypeError):
        ax = task_func(l)