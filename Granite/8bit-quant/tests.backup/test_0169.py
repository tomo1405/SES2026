import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src_0169 import task_func
import pytest

def test_task_func():
    # Test with default arguments
    fig, data, plot_filename = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename == 'test_plot.png'
    assert len(data.columns) == 5
    assert all(data.columns == [f'Group{i + 1}' for i in range(5)])
    assert data.shape == (5, 5)

    # Test with custom arguments
    fig, data, plot_filename = task_func(num_groups=3, data_size=10, labels=['A', 'B', 'C'])
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename == 'test_plot.png'
    assert len(data.columns) == 3
    assert all(data.columns == ['A', 'B', 'C'])
    assert data.shape == (10, 3)