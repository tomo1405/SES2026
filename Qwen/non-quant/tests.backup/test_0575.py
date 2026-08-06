import pytest
from src_0575 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_output():
    ax = task_func()
    assert isinstance(ax, plt.Axes)

def test_task_func_plot_data():
    ax = task_func()
    lines = ax.get_lines()
    assert len(lines) == 2, "There should be two lines in the plot: data and fit."

def test_task_func_plot_labels():
    ax = task_func()
    assert ax.get_xlabel() == 'x', "X-axis label should be 'x'."
    assert ax.get_ylabel() == 'y', "Y-axis label should be 'y'."

def test_task_func_legend():
    ax = task_func()
    legend = ax.get_legend()
    assert legend is not None, "Legend should be present."
    texts = [text.get_text() for text in legend.get_texts()]
    assert 'data' in texts, "'data' should be in the legend."
    assert 'fit' in texts[1], "'fit' should be in the legend."

def test_task_func_curve_fit_parameters():
    ax = task_func(array_length=100, noise_level=0.2)
    lines = ax.get_lines()
    fit_line = lines[1]
    label = fit_line.get_label()
    a, b = map(float, label.split('=')[1].split(','))
    assert a > 0 and a < 2, "Parameter 'a' should be close to 1."
    assert b > 0 and b < 2, "Parameter 'b' should be close to 1."