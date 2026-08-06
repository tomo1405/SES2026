import pytest
import matplotlib.pyplot as plt
import random

from src_0367 import task_func

COLORS = ['#00bfbf', '#000000', '#0000ff']

def test_task_func():
    number_list = [random.randint(1, 100) for _ in range(100)]
    bins = 10
    ax = task_func(number_list, bins)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram'
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, 2, 'a'], 2)

def test_task_func_with_invalid_bins():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], 'abc')