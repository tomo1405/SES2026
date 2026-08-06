import pytest
from src_0905 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import matplotlib.backends.backend_agg as agg

def test_task_func_with_default_keys():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # One line for each key: 'x', 'y', 'z'

def test_task_func_with_custom_keys():
    data = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
    ax = task_func(data, keys=['a', 'b'])
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # Only 'a' and 'b' should be plotted

def test_task_func_with_missing_keys():
    data = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
    ax = task_func(data, keys=['d', 'e'])
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0  # No lines should be plotted

def test_task_func_with_no_data():
    data = []
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0  # No lines should be plotted

def test_task_func_with_single_entry():
    data = [{'x': 1, 'y': 2, 'z': 3}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # One line for each key: 'x', 'y', 'z'

def test_task_func_plot_output():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    
    # Capture the plot output
    buf = io.BytesIO()
    canvas = agg.FigureCanvasAgg(ax.figure)
    canvas.print_png(buf)
    buf.seek(0)
    
    # Check that the buffer is not empty (indicating a plot was created)
    assert buf.getbuffer().nbytes > 0