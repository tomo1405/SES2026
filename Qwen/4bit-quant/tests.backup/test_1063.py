import pytest
from src_1063 import task_func
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from io import BytesIO
import matplotlib.pyplot as plt

@pytest.fixture
def empty_array():
    return np.array([])

@pytest.fixture
def non_empty_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func_with_empty_array(empty_array):
    ax = task_func(empty_array)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Time Series of Row Sums"

def test_task_func_with_non_empty_array(non_empty_array):
    ax = task_func(non_empty_array)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    
    # Check if the plot contains the correct data
    fig = ax.get_figure()
    buf = BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    loaded_fig = Figure()
    loaded_fig.from_string(buf.read())
    assert len(loaded_fig.axes) == 1
    assert loaded_fig.axes[0].get_lines()[0].get_data()[1] == np.array([6, 15, 24])

def test_task_func_with_single_row_array():
    arr = np.array([[1, 2, 3]])
    ax = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    
    # Check if the plot contains the correct data
    fig = ax.get_figure()
    buf = BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    loaded_fig = Figure()
    loaded_fig.from_string(buf.read())
    assert len(loaded_fig.axes) == 1
    assert loaded_fig.axes[0].get_lines()[0].get_data()[1] == np.array([6])

def test_task_func_with_single_column_array():
    arr = np.array([[1], [2], [3]])
    ax = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    
    # Check if the plot contains the correct data
    fig = ax.get_figure()
    buf = BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    loaded_fig = Figure()
    loaded_fig.from_string(buf.read())
    assert len(loaded_fig.axes) == 1
    assert loaded_fig.axes[0].get_lines()[0].get_data()[1] == np.array([1, 2, 3])