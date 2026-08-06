import pytest
from src_0905 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_basic():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_missing_keys():
    data = [{'x': 1, 'y': 2}, {'x': 4, 'y': 5}]
    ax = task_func(data, keys=['x', 'y', 'z'])
    assert isinstance(ax, plt.Axes)
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert 'x' in legend_labels
    assert 'y' in legend_labels
    assert 'z' not in legend_labels

def test_task_func_no_data():
    data = []
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0

def test_task_func_single_point():
    data = [{'x': 1, 'y': 2, 'z': 3}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3

def test_task_func_plot_content():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    x_line = ax.lines[0]
    y_line = ax.lines[1]
    z_line = ax.lines[2]
    assert (x_line.get_xdata() == [1, 4]).all()
    assert (x_line.get_ydata() == [2, 5]).all()
    assert (y_line.get_xdata() == [1, 4]).all()
    assert (y_line.get_ydata() == [2, 5]).all()
    assert (z_line.get_xdata() == [1, 4]).all()
    assert (z_line.get_ydata() == [3, 6]).all()

def test_task_func_plot_legend():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert 'x' in legend_labels
    assert 'y' in legend_labels
    assert 'z' in legend_labels

def test_task_func_plot_savefig():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    buf = BytesIO()
    ax.figure.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert len(img_str) > 0

def test_task_func_empty_keys():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data, keys=[])
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0

def test_task_func_nonexistent_keys():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data, keys=['a', 'b', 'c'])
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0