import matplotlib.pyplot as plt
import pandas as pd
from src_0169 import task_func


def test_task_func():
    # Test with default labels
    fig, data, plot_filename = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename.endswith('.png')

    # Test with custom labels
    labels = ['A', 'B', 'C', 'D', 'E']
    fig, data, plot_filename = task_func(labels=labels)
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename.endswith('.png')

    # Test with different data size
    data_size = 10
    fig, data, plot_filename = task_func(data_size=data_size)
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename.endswith('.png')
    assert data.shape[0] == data_size

    # Test with different number of groups
    num_groups = 3
    fig, data, plot_filename = task_func(num_groups=num_groups)
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename.endswith('.png')
    assert data.shape[1] == num_groups