import heapq
import math
import matplotlib.pyplot as plt
import pytest

from src_0198 import task_func

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5, 6]
    N = 3

    largest_diff_indices = heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]

    ax = task_func(l1, l2, N)

    assert ax is not None
    assert ax.get_lines() == [largest_diffs]

def test_task_func_with_default_N():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5, 6]

    largest_diff_indices = heapq.nlargest(10, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]

    ax = task_func(l1, l2)

    assert ax is not None
    assert ax.get_lines() == [largest_diffs]

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, 2], [3, 4, 5])