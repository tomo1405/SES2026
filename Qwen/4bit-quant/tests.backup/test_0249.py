import pytest
from src_0249 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_valid_data():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # Two lines for two columns of data
    assert ax.get_legend().get_texts()[0].get_text() == 'Position 1'
    assert ax.get_legend().get_texts()[1].get_text() == 'Position 2'

def test_task_func_with_single_column():
    data_list = [[1, 2, 3]]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0  # No lines for a single column of data

def test_task_func_with_empty_data_list():
    with pytest.raises(ValueError) as excinfo:
        task_func([])
    assert str(excinfo.value) == 'Empty data_list'

def test_task_func_with_missing_values():
    data_list = [[1, 2], [3, 4, 5]]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1  # One line for one column of data
    assert np.isnan(ax.lines[0].get_ydata()[2])  # Check for NaN in the last position

def test_task_func_with_no_data():
    data_list = [[np.nan, np.nan], [np.nan, np.nan]]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1  # One line for one column of data
    assert np.all(np.isnan(ax.lines[0].get_ydata()))  # All values should be NaN