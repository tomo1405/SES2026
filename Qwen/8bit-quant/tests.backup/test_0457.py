import pytest
from src_0457 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    })

def test_task_func_normalization(sample_data):
    normalized_data, _ = task_func(sample_data)
    assert isinstance(normalized_data, pd.DataFrame)
    assert normalized_data.shape == sample_data.shape
    assert normalized_data.min().min() >= 0
    assert normalized_data.max().max() <= 1

def test_task_func_plot(sample_data):
    _, ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == ''
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''

def test_task_func_cmap(sample_data):
    _, ax = task_func(sample_data)
    assert ax.collections[0].cmap.name == 'YlGnBu'

def test_task_func_cbar_label(sample_data):
    _, ax = task_func(sample_data)
    assert ax.collections[0].cbar.ax.get_ylabel() == 'Normalized Value'

def test_task_func_figsize(sample_data):
    _, ax = task_func(sample_data)
    fig = ax.get_figure()
    assert fig.get_size_inches() == (10, 8)