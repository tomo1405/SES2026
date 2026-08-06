python
import pytest
from src_0169 import task_func

def test_task_func():
    # Test default values
    fig, data, plot_filename = task_func()
    assert len(data.columns) == 5
    assert len(data) == 5
    assert plot_filename == 'test_plot.png'

    # Test custom values
    fig, data, plot_filename = task_func(num_groups=3, data_size=4, labels=['A', 'B', 'C'])
    assert len(data.columns) == 3
    assert len(data) == 4
    assert plot_filename == 'test_plot.png'
    assert list(data.columns) == ['A', 'B', 'C']