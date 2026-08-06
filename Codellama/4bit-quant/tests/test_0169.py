import pytest
from src_0169 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    # Test with default arguments
    fig, data, plot_filename = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename.endswith('.png')

    # Test with custom arguments
    fig, data, plot_filename = task_func(num_groups=3, data_size=10, labels=['A', 'B', 'C'])
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename.endswith('.png')

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(num_groups=0, data_size=10, labels=['A', 'B', 'C'])
    with pytest.raises(ValueError):
        task_func(num_groups=3, data_size=0, labels=['A', 'B', 'C'])
    with pytest.raises(ValueError):
        task_func(num_groups=3, data_size=10, labels=[])