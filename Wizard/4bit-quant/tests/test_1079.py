python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(arr):
    unique, counts = np.unique(arr, return_counts=True)
    uniform_distribution = len(set(counts)) == 1

    _, ax = plt.subplots()
    ax.hist(arr, bins=np.arange(len(unique) + 1) - 0.5, rwidth=0.8, align="mid")
    ax.set_xticks(range(len(unique)))
    ax.set_xticklabels(unique)

    return uniform_distribution, ax

def test_task_func():
    # Test case 1
    arr = np.array([1, 2, 3, 4, 5])
    expected_uniform_distribution = True
    expected_ax_title = "Histogram"
    expected_ax_xlabel = "Values"
    expected_ax_ylabel = "Frequency"

    uniform_distribution, ax = task_func(arr)

    assert uniform_distribution == expected_uniform_distribution
    assert ax.get_title() == expected_ax_title
    assert ax.get_xlabel() == expected_ax_xlabel
    assert ax.get_ylabel() == expected_ax_ylabel

    # Test case 2
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected_uniform_distribution = False
    expected_ax_title = "Histogram"
    expected_ax_xlabel = "Values"
    expected_ax_ylabel = "Frequency"

    uniform_distribution, ax = task_func(arr)

    assert uniform_distribution == expected_uniform_distribution
    assert ax.get_title() == expected_ax_title
    assert ax.get_xlabel() == expected_ax_xlabel
    assert ax.get_ylabel() == expected_ax_ylabel