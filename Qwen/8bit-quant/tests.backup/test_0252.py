import pytest
from src_0252 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'Job': ['Engineer', 'Doctor', 'Engineer', 'Artist', 'Doctor', 'Engineer']
    }
    return pd.DataFrame(data)

def test_task_func_input_type(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data.to_dict())

def test_task_func_output_type(sample_data):
    fig = task_func(sample_data)
    assert isinstance(fig, plt.Figure)

def test_task_func_pie_chart_labels(sample_data):
    fig = task_func(sample_data)
    ax = fig.axes[0]
    labels = [text.get_text() for text in ax.get_xticklabels()]
    expected_labels = ['Engineer', 'Doctor', 'Artist']
    assert set(labels) == set(expected_labels)

def test_task_func_pie_chart_sizes(sample_data):
    fig = task_func(sample_data)
    ax = fig.axes[0]
    wedges = ax.patches
    sizes = [wedge.get_width() for wedge in wedges]
    expected_sizes = [3/6, 2/6, 1/6]
    assert sizes == expected_sizes

def test_task_func_pie_chart_colors(sample_data):
    fig = task_func(sample_data)
    ax = fig.axes[0]
    wedges = ax.patches
    colors = [wedge.get_facecolor() for wedge in wedges]
    expected_colors = [plt.cm.Spectral(i/3) for i in range(3)]
    assert all([c1 == c2 for c1, c2 in zip(colors, expected_colors)])