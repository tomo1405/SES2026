import pytest
from src_0583 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_output():
    fig = task_func()
    assert isinstance(fig, plt.Figure), "The function should return a matplotlib Figure object."

def test_task_func_data_distribution():
    data = task_func(size=1000).get_axes()[0].patches
    assert len(data) > 0, "The histogram should have at least one bin."
    
    # Check if the number of bins is correct
    bin_edges = np.histogram_bin_edges(task_func(size=1000).get_axes()[0].lines[0].get_xdata(), bins='auto')
    number_of_bins = len(bin_edges) - 1
    assert len(data) == number_of_bins, "The number of bins in the histogram does not match the calculated number of bins."

def test_task_func_plot_lines():
    fig = task_func()
    lines = fig.get_axes()[0].lines
    assert len(lines) == 1, "The plot should have exactly one line (the normal distribution curve)."
    assert lines[0].get_color() == 'k', "The line color should be black."
    assert lines[0].get_linewidth() == 2, "The line width should be 2."

def test_task_func_histogram_properties():
    fig = task_func()
    hist = fig.get_axes()[0].patches
    assert all(patch.get_alpha() == 0.6 for patch in hist), "The alpha value of each bar in the histogram should be 0.6."
    assert all(patch.get_facecolor() == (0.0, 0.6, 0.0, 1.0) for patch in hist), "The color of each bar in the histogram should be green."

def test_task_func_with_different_size():
    fig = task_func(size=500)
    data = fig.get_axes()[0].patches
    assert len(data) > 0, "The histogram should have at least one bin when size is 500."
    
    # Check if the number of bins is correct
    bin_edges = np.histogram_bin_edges(fig.get_axes()[0].lines[0].get_xdata(), bins='auto')
    number_of_bins = len(bin_edges) - 1
    assert len(data) == number_of_bins, "The number of bins in the histogram does not match the calculated number of bins when size is 500."