import pytest
from src_0165 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

@pytest.fixture
def expected_data():
    np.random.seed(0)
    columns = [f'Label{i + 1}' for i in range(5)]
    return pd.DataFrame(np.random.uniform(0, 1, size=(5, 5)), columns=columns)

def test_task_func_returns_figure_object(expected_data):
    fig = task_func()
    assert isinstance(fig, plt.Figure)

def test_task_func_dataframe_shape(expected_data):
    fig = task_func()
    ax = fig.axes[0]
    plotted_data = pd.DataFrame(ax.patches).get_widths().reshape((5, 5))
    assert plotted_data.shape == expected_data.shape

def test_task_func_dataframe_values(expected_data):
    fig = task_func()
    ax = fig.axes[0]
    plotted_data = pd.DataFrame(ax.patches).get_widths().reshape((5, 5))
    np.testing.assert_almost_equal(plotted_data, expected_data.values)

def test_task_func_with_custom_num_labels():
    fig = task_func(num_labels=3)
    ax = fig.axes[0]
    assert len(ax.patches) == 9

def test_task_func_with_custom_data_range():
    fig = task_func(data_range=(10, 20))
    ax = fig.axes[0]
    plotted_data = pd.DataFrame(ax.patches).get_widths().reshape((5, 5))
    assert plotted_data.min() >= 10 and plotted_data.max() <= 20

def test_task_func_plot_kind(expected_data):
    fig = task_func()
    ax = fig.axes[0]
    assert ax.get_legend().get_texts()[0].get_text() == 'Label1'

def test_task_func_stacked_bar_chart(expected_data):
    fig = task_func()
    ax = fig.axes[0]
    assert ax.get_legend().get_texts()[-1].get_text() == 'Label5'