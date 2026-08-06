import pytest
from src_0169 import task_func

def test_task_func():
    # Test with default arguments
    fig, data, plot_filename = task_func()
    assert isinstance(fig, object)
    assert isinstance(data, object)
    assert isinstance(plot_filename, str)
    assert plot_filename == 'test_plot.png'

    # Test with custom arguments
    fig, data, plot_filename = task_func(num_groups=3, data_size=10, labels=['A', 'B', 'C'])
    assert isinstance(fig, object)
    assert isinstance(data, object)
    assert isinstance(plot_filename, str)
    assert plot_filename == 'test_plot.png'