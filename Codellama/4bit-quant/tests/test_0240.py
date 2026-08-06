import pytest
from src_0240 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, computed_stats, ax = task_func(original)
    assert np.array_equal(arr, np.array([2, 4, 6]))
    assert computed_stats['mean'] == 4
    assert computed_stats['std'] == 2
    assert computed_stats['min'] == 2
    assert computed_stats['max'] == 6
    assert ax.get_title() == 'Histogram with PDF'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_legend() == 'Histogram'
    assert ax.get_legend() == 'PDF'
    plt.close(fig)