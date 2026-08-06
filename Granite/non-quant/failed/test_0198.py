import heapq
import math
import matplotlib.pyplot as plt
from unittest.mock import patch

def task_func(l1, l2, N=10):
    largest_diff_indices = heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]

    fig, ax = plt.subplots()
    ax.plot(largest_diffs)

    return ax

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5, 6]
    ax = task_func(l1, l2)
    assert ax is not None
    assert ax.get_lines()

def test_task_func_with_mock():
    with patch('matplotlib.pyplot.show') as mock_show:
        l1 = [1, 2, 3, 4, 5]
        l2 = [2, 3, 4, 5, 6]
        ax = task_func(l1, l2)
        mock_show.assert_called_once()