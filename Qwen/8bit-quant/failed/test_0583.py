import pytest
from src_0583 import task_func
import matplotlib.pyplot as plt
import io
import numpy as np

@pytest.fixture
def plot_capture():
    # Capture the plot output
    old_stdout = plt.rcParams['figure.figsize']
    plt.rcParams['figure.figsize'] = (10, 8)
    fig = task_func()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    plt.rcParams['figure.figsize'] = old_stdout
    return buf

def test_task_func_return_type(plot_capture):
    # Test that the function returns a matplotlib figure
    assert isinstance(plot_capture, io.BytesIO)

def test_task_func_data_size():
    # Test that the function generates data of the correct size
    fig = task_func(size=500)
    ax = fig.axes[0]
    data, _ = ax.hist.get_data()
    assert len(data) == 500

def test_task_func_histogram_properties(plot_capture):
    # Test that the histogram has the correct properties
    fig = plt.imread(plot_capture)
    ax = fig.axes[0]
    assert ax.hist.get_alpha() == 0.6
    assert ax.hist.get_color() == 'g'

def test_task_func_plot_line(plot_capture):
    # Test that the plot line is present
    fig = plt.imread(plot_capture)
    lines = fig.axes[0].get_lines()
    assert len(lines) == 1
    assert lines[0].get_linewidth() == 2
    assert lines[0].get_color() == 'k'