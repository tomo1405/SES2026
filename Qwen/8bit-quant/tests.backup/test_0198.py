import pytest
from src_0198 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with simple lists
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 4, 3, 2, 1]
    ax = task_func(l1, l2, N=3)
    expected_diffs = [np.sqrt((1-5)**2), np.sqrt((2-4)**2), np.sqrt((3-3)**2)]
    assert np.allclose(ax.lines[0].get_ydata(), sorted(expected_diffs, reverse=True)[:3])

    # Test with identical lists
    l1 = [1, 1, 1, 1, 1]
    l2 = [1, 1, 1, 1, 1]
    ax = task_func(l1, l2, N=3)
    expected_diffs = [0, 0, 0]
    assert np.allclose(ax.lines[0].get_ydata(), expected_diffs)

    # Test with different lengths of lists (l1 longer than l2)
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [5, 4, 3, 2]
    ax = task_func(l1, l2, N=3)
    expected_diffs = [np.sqrt((1-5)**2), np.sqrt((2-4)**2), np.sqrt((3-3)**2)]
    assert np.allclose(ax.lines[0].get_ydata(), sorted(expected_diffs, reverse=True)[:3])

    # Test with different lengths of lists (l2 longer than l1)
    l1 = [1, 2, 3, 4]
    l2 = [5, 4, 3, 2, 1, 0]
    ax = task_func(l1, l2, N=3)
    expected_diffs = [np.sqrt((1-5)**2), np.sqrt((2-4)**2), np.sqrt((3-3)**2)]
    assert np.allclose(ax.lines[0].get_ydata(), sorted(expected_diffs, reverse=True)[:3])

    # Test with negative numbers
    l1 = [-1, -2, -3, -4, -5]
    l2 = [-5, -4, -3, -2, -1]
    ax = task_func(l1, l2, N=3)
    expected_diffs = [np.sqrt((-1+5)**2), np.sqrt((-2+4)**2), np.sqrt((-3+3)**2)]
    assert np.allclose(ax.lines[0].get_ydata(), sorted(expected_diffs, reverse=True)[:3])

    # Clean up plot after tests
    plt.close('all')