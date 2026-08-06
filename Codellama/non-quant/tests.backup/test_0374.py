import pytest
from src_0374 import task_func

def test_task_func():
    x_data = [1, 2, 3, 4, 5]
    l = [1, 2, 3, 4, 5]
    params, fitted_values = task_func(l, x_data)
    assert params[0] == 1
    assert params[1] == 2
    assert fitted_values[0] == 1
    assert fitted_values[1] == 4
    assert fitted_values[2] == 9
    assert fitted_values[3] == 16
    assert fitted_values[4] == 25

def test_task_func_plot():
    x_data = [1, 2, 3, 4, 5]
    l = [1, 2, 3, 4, 5]
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert params[0] == 1
    assert params[1] == 2
    assert fitted_values[0] == 1
    assert fitted_values[1] == 4
    assert fitted_values[2] == 9
    assert fitted_values[3] == 16
    assert fitted_values[4] == 25
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Fitted function'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_label() == 'Data'
    assert ax.get_lines()[1].get_label() == 'Fitted function'
    assert ax.get_legend().get_title() == 'Legend'
    assert len(ax.get_legend().get_texts()) == 2
    assert ax.get_legend().get_texts()[0].get_text() == 'Data'
    assert ax.get_legend().get_texts()[1].get_text() == 'Fitted function'