import pytest
from src_0905 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_with_default_keys():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # Three lines for 'x', 'y', 'z'
    assert ax.get_legend().get_texts()[0].get_text() == 'x'
    assert ax.get_legend().get_texts()[1].get_text() == 'y'
    assert ax.get_legend().get_texts()[2].get_text() == 'z'

def test_task_func_with_custom_keys():
    data = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
    ax = task_func(data, keys=['a', 'b'])
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # Two lines for 'a', 'b'
    assert ax.get_legend().get_texts()[0].get_text() == 'a'
    assert ax.get_legend().get_texts()[1].get_text() == 'b'

def test_task_func_with_missing_keys():
    data = [{'x': 1, 'y': 2}, {'x': 4, 'y': 5}]
    ax = task_func(data, keys=['x', 'y', 'z'])
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # Two lines for 'x', 'y'
    assert ax.get_legend().get_texts()[0].get_text() == 'x'
    assert ax.get_legend().get_texts()[1].get_text() == 'y'

def test_task_func_with_no_data():
    data = []
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0  # No lines plotted
    assert ax.get_legend() is None

def test_task_func_with_single_data_point():
    data = [{'x': 1, 'y': 2, 'z': 3}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # Three lines for 'x', 'y', 'z'
    assert ax.get_legend().get_texts()[0].get_text() == 'x'
    assert ax.get_legend().get_texts()[1].get_text() == 'y'
    assert ax.get_legend().get_texts()[2].get_text() == 'z'

def test_task_func_plot_output():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(data)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert len(image_base64) > 0  # Ensure the plot is generated and saved correctly