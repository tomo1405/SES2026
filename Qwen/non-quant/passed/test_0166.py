import pytest
from src_0166 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def test_task_func_default():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 5 * 5  # 5 columns with 5 rows each

def test_task_func_custom_rows():
    num_rows = 10
    fig = task_func(num_rows=num_rows)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 5 * num_rows  # 5 columns with 10 rows each

def test_task_func_custom_range():
    rand_range = (10, 20)
    fig = task_func(rand_range=rand_range)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert isinstance(ax, plt.Axes)
    for patch in ax.patches:
        assert rand_range[0] <= patch.get_height() <= rand_range[1]

def test_task_func_plot_content():
    fig = task_func()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert image_base64  # Ensure that the image is not empty

def test_task_func_labels():
    fig = task_func()
    ax = fig.axes[0]
    assert ax.get_legend().get_texts()[0].get_text() == 'A'
    assert ax.get_legend().get_texts()[1].get_text() == 'B'
    assert ax.get_legend().get_texts()[2].get_text() == 'C'
    assert ax.get_legend().get_texts()[3].get_text() == 'D'
    assert ax.get_legend().get_texts()[4].get_text() == 'E'