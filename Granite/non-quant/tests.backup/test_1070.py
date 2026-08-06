import pandas as pd
import matplotlib.pyplot as plt
import pytest
from src_1070 import task_func

@pytest.fixture
def data_dict():
    return {'column1': ['A', 'B', 'C', 'D', 'E'],
            'column2': ['F', 'G', 'H', 'I', 'J'],
            'column3': ['K', 'L', 'M', 'N', 'O']}

def test_task_func(data_dict):
    axes_list = task_func(data_dict)
    assert len(axes_list) == len(data_dict.keys())
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

def test_uniform_distribution(data_dict):
    axes_list = task_func(data_dict)
    for ax in axes_list:
        yticks = ax.get_yticks()
        assert len(set(yticks)) == 1

def test_column_names(data_dict):
    axes_list = task_func(data_dict)
    for ax, column in zip(axes_list, data_dict.keys()):
        assert ax.get_title() == column