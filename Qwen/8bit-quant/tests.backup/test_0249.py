import pytest
from src_0249 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_valid_data():
    data_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # Two lines plotted (ignoring the first column)

def test_task_func_with_empty_data_list():
    with pytest.raises(ValueError, match='Empty data_list'):
        task_func([])

def test_task_func_with_single_column():
    data_list = [[1, 2, 3]]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0  # No lines plotted (only one column)

def test_task_func_with_different_lengths():
    data_list = [
        [1, 2],
        [3, 4, 5],
        [6, 7]
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # Two lines plotted (ignoring the first column)

def test_task_func_with_nan_fillvalue():
    data_list = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # Two lines plotted (ignoring the first column)