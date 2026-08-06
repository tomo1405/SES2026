import pytest
from src_0249 import task_func
import numpy as np
import matplotlib.pyplot as plt
import itertools

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(data_list)
    assert ax is not None
    assert isinstance(ax, plt.Axes)
    assert ax.get_legend_handles_labels() == ([<Line2D at 0x7f22c4d11d60>, <Line2D at 0x7f22c4d11d90>], ['Position 1', 'Position 2'])

def test_task_func_empty_data_list():
    with pytest.raises(ValueError):
        task_func([])