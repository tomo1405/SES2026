import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_1070 import task_func

@pytest.fixture
def data_dict():
    return {'column1': [1, 2, 3, 4, 5], 'column2': ['a', 'b', 'c', 'd', 'e']}

def test_task_func(data_dict):
    axes_list = task_func(data_dict)
    assert len(axes_list) == 2
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

def test_uniform_distribution(data_dict):
    axes_list = task_func(data_dict)
    for ax in axes_list:
        ax.figure.canvas.draw()
        lines = ax.get_lines()
        counts = lines[0].get_ydata()
        assert len(set(counts)) == 1

def test_non_uniform_distribution(data_dict):
    data_dict['column2'] = ['a', 'a', 'a', 'a', 'a']
    with pytest.warns(UserWarning, match="not uniform"):
        task_func(data_dict)