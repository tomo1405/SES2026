import pytest
from src_0238 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_no_save_plot():
    data = [('item1', 1, 2, 3), ('item2', 4, 5, 6)]
    result = task_func(data, save_plot=False)
    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 2)

def test_task_func_save_plot_with_path():
    data = [('item1', 1, 2, 3), ('item2', 4, 5, 6)]
    plot_path = 'test_plot.png'
    result, ax = task_func(data, save_plot=True, plot_path=plot_path)
    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 2)
    assert isinstance(ax, plt.Axes)
    assert plt.fignum_exists(1) is False  # Figure should be closed

def test_task_func_save_plot_without_path():
    data = [('item1', 1, 2, 3), ('item2', 4, 5, 6)]
    with pytest.raises(ValueError, match="plot_path is required if save_plot is True"):
        task_func(data, save_plot=True, plot_path=None)

def test_task_func_empty_data():
    data = []
    result = task_func(data, save_plot=False)
    assert isinstance(result, np.ndarray)
    assert result.shape == (0, 2)

def test_task_func_single_item():
    data = [('item1', 1, 2, 3)]
    result = task_func(data, save_plot=False)
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 2)