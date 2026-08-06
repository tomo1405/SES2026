import pytest
from src_0376 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[2.5, 2.4],
                     [0.5, 0.7],
                     [2.2, 2.9],
                     [1.9, 2.2],
                     [3.1, 3.0],
                     [2.3, 2.7],
                     [2, 1.6],
                     [1, 1.1],
                     [1.5, 1.6],
                     [1.1, 0.9]])

def test_task_func_output_type(sample_data):
    ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot_content(sample_data):
    ax = task_func(sample_data)
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line (scatter plot) in the Axes"
    xdata = lines[0].get_xdata()
    ydata = lines[0].get_ydata()
    assert len(xdata) == len(sample_data), "The number of xdata points should match the number of input samples"
    assert len(ydata) == len(sample_data), "The number of ydata points should match the number of input samples"

def test_task_func_plot_labels(sample_data):
    ax = task_func(sample_data)
    assert ax.get_xlabel() == 'First Principal Component', "X-axis label should be 'First Principal Component'"
    assert ax.get_ylabel() == 'Second Principal Component', "Y-axis label should be 'Second Principal Component'"
    assert ax.get_title() == 'PCA Result', "Title should be 'PCA Result'"

def test_task_func_plot_size(sample_data):
    ax = task_func(sample_data)
    fig = ax.get_figure()
    assert fig.get_size_inches()[0] == 6, "Figure width should be 6 inches"
    assert fig.get_size_inches()[1] == 4, "Figure height should be 4 inches"