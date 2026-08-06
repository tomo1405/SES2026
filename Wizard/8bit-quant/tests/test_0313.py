python
import random
import matplotlib.pyplot as plt
import pytest

# Constants
DISTRIBUTION_SIZE = 1000

def task_func(bins=30):

    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    ax = plt.hist(distribution, bins=bins, edgecolor='black')[2]
    return distribution, ax

def test_task_func():
    distribution, ax = task_func()
    assert len(distribution) == DISTRIBUTION_SIZE
    assert len(ax.patches) == bins