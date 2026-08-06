import pytest
from src_0313 import task_func
import random
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Default bins
    distribution, ax = task_func()
    assert isinstance(distribution, list)
    assert len(distribution) == DISTRIBUTION_SIZE
    assert isinstance(ax, plt.Axes)

    # Test case 2: Custom bins
    bins = 50
    distribution, ax = task_func(bins=bins)
    assert isinstance(distribution, list)
    assert len(distribution) == DISTRIBUTION_SIZE
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == bins