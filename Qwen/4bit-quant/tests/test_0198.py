import pytest
from src_0198 import task_func
import numpy as np

def test_task_func_with_equal_lists():
    l1 = [1, 2, 3, 4, 5]
    l2 = [1, 2, 3, 4, 5]
    ax = task_func(l1, l2)
    assert len(ax.lines) == 1
    assert np.allclose(ax.lines[0].get_ydata(), np.zeros(10))

def test_task_func_with_different_lists():
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 4, 3, 2, 1]
    ax = task_func(l1, l2)
    assert len(ax.lines) == 1
    assert np.allclose(ax.lines[0].get_ydata(), np.array([4, 3, 2, 1, 0]))

def test_task_func_with_custom_N():
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 4, 3, 2, 1]
    N = 3
    ax = task_func(l1, l2, N=N)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_ydata()) == N

def test_task_func_with_negative_numbers():
    l1 = [-1, -2, -3, -4, -5]
    l2 = [-5, -4, -3, -2, -1]
    ax = task_func(l1, l2)
    assert len(ax.lines) == 1
    assert np.allclose(ax.lines[0].get_ydata(), np.array([4, 3, 2, 1, 0]))

def test_task_func_with_mixed_positive_and_negative_numbers():
    l1 = [1, -2, 3, -4, 5]
    l2 = [-5, 4, -3, 2, -1]
    ax = task_func(l1, l2)
    assert len(ax.lines) == 1
    assert np.allclose(ax.lines[0].get_ydata(), np.array([6, 6, 6, 6, 6]))