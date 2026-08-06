import pandas as pd
from src_0169 import task_func


def test_task_func():
    # Test with default arguments
    fig, data, plot_filename = task_func()
    assert isinstance(fig, object)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename == 'test_plot.png'

    # Test with custom arguments
    num_groups = 3
    data_size = 10
    labels = ['A', 'B', 'C']
    fig, data, plot_filename = task_func(num_groups=num_groups, data_size=data_size, labels=labels)
    assert isinstance(fig, object)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename == 'test_plot.png'
    assert data.shape == (data_size, num_groups)
    assert data.columns.tolist() == labels