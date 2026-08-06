import pytest
from src_0198 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 4, 3, 2, 1]
    N = 3

    ax = task_func(l1, l2, N)

    # Check that the plot has the correct number of points
    assert len(ax.lines[0].get_data()[0]) == N

    # Check that the differences are calculated correctly
    expected_diffs = [np.sqrt((l1[i] - l2[i])**2) for i in heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))]
    actual_diffs = ax.lines[0].get_data()[1]
    assert np.allclose(expected_diffs, actual_diffs)

    # Check that the plot is created correctly
    assert isinstance(ax, plt.Axes)