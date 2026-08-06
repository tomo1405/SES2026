import pytest
from src_0374 import task_func

def test_task_func():
    x_data = [1, 2, 3, 4, 5]
    l = [1, 2, 3, 4, 5]
    params, fitted_values = task_func(l, x_data)
    assert params == (1, 2)
    assert fitted_values == [1, 4, 9, 16, 25]

def test_task_func_plot():
    x_data = [1, 2, 3, 4, 5]
    l = [1, 2, 3, 4, 5]
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert params == (1, 2)
    assert fitted_values == [1, 4, 9, 16, 25]
    assert ax.get_title() == 'Fitted function'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_legend() == 'Data'
    assert ax.get_legend() == 'Fitted function'