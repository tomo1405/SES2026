import pytest
from src_0374 import task_func

def test_task_func_with_plot():
    l = [1, 2, 3, 4, 5]
    x_data = [1, 2, 3, 4, 5]
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert isinstance(params, tuple)
    assert isinstance(fitted_values, list)
    assert isinstance(ax, object)

def test_task_func_without_plot():
    l = [1, 2, 3, 4, 5]
    x_data = [1, 2, 3, 4, 5]
    params, fitted_values = task_func(l, x_data, plot=False)
    assert isinstance(params, tuple)
    assert isinstance(fitted_values, list)

def test_task_func_with_invalid_input():
    l = [1, 2, 3, 4, 5]
    x_data = [1, 2, 3, 4]
    with pytest.raises(ValueError):
        task_func(l, x_data, plot=False)