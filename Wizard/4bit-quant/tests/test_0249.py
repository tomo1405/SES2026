python
import itertools
import numpy as np
import matplotlib.pyplot as plt
import pytest

from src_0249 import task_func

def test_task_func():
    data_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Position 1'
    assert ax.get_ylabel() == 'Position 2'
    assert ax.get_title() == 'Position 3'
    assert ax.get_legend_handles_labels()[0] == ['Position 1', 'Position 2', 'Position 3']
    assert ax.get_legend_handles_labels()[1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert ax.get_ylim() == (1, 12)
    assert ax.get_xlim() == (0, 3)
    assert ax.get_xticks() == [0, 1, 2, 3]
    assert ax.get_yticks() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert ax.get_xticklabels() == ['0', '1', '2', '3']
    assert ax.get_yticklabels() == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    assert ax.get_legend()._loc == 2
    
    data_list = []
    with pytest.raises(ValueError):
        task_func(data_list)