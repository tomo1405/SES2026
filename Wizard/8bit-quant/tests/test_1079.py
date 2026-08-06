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
    arr = np.array([1, 2, 3, 4, 5])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == True
    assert ax.get_xlabel() == '1'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram'
    assert ax.get_xticks() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels() == ['1', '2', '3', '4', '5']
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_yticklabels() == ['0', '1', '2', '3', '4', '5']