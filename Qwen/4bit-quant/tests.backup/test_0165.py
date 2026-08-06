import pytest
from src_0165 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.patches) == 25  # 5 labels * 5 bars each

def test_task_func_custom_num_labels():
    fig = task_func(num_labels=3)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.patches) == 9  # 3 labels * 3 bars each

def test_task_func_custom_data_range():
    fig = task_func(data_range=(-1, 1))
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.patches) == 25  # 5 labels * 5 bars each

def test_task_func_reproducibility():
    fig1 = task_func()
    fig2 = task_func()
    assert fig1 == fig2  # Check if the figures are identical

def test_task_func_with_seed_reset():
    np.random.seed(0)
    fig1 = task_func()
    np.random.seed(0)
    fig2 = task_func()
    assert fig1 == fig2  # Check if resetting the seed produces identical figures

def test_task_func_plot_type():
    fig = task_func()
    ax = fig.axes[0]
    assert ax.get_legend() is not None  # Stacked bar plot should have a legend
    assert len(ax.get_legend().get_texts()) == 5  # 5 labels in the legend

def test_task_func_dataframe_content():
    np.random.seed(0)
    data = pd.DataFrame(np.random.uniform(0, 1, size=(5, 5)), columns=[f'Label{i + 1}' for i in range(5)])
    fig = task_func()
    ax = fig.axes[0]
    plotted_data = pd.DataFrame([[patch.get_height() for patch in bar] for bar in ax.containers])
    pd.testing.assert_frame_equal(plotted_data, data)