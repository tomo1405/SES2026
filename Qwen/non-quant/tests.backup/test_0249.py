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
    lines = ax.get_lines()
    assert len(lines) == 2
    assert lines[0].get_label() == 'Position 1'
    assert lines[1].get_label() == 'Position 2'
    assert np.array_equal(lines[0].get_ydata(), np.array([2, 5, 8]))
    assert np.array_equal(lines[1].get_ydata(), np.array([3, 6, 9]))

def test_task_func_with_empty_data():
    with pytest.raises(ValueError, match='Empty data_list'):
        task_func([])

def test_task_func_with_data_of_different_lengths():
    data_list = [
        [1, 2, 3],
        [4, 5],
        [7, 8, 9, 10]
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    lines = ax.get_lines()
    assert len(lines) == 2
    assert lines[0].get_label() == 'Position 1'
    assert lines[1].get_label() == 'Position 2'
    assert np.array_equal(lines[0].get_ydata(), np.array([2, 5, np.nan, np.nan]))
    assert np.array_equal(lines[1].get_ydata(), np.array([3, np.nan, 9, 10]))

def test_task_func_with_single_column_data():
    data_list = [
        [1, 2, 3]
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    lines = ax.get_lines()
    assert len(lines) == 0

def test_task_func_with_no_data():
    data_list = [[]]
    with pytest.raises(ValueError, match='Empty data_list'):
        task_func(data_list)