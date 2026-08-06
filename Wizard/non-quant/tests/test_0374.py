python
import pytest
from src_0374 import task_func

def test_task_func():
    x_data = [1, 2, 3, 4, 5]
    l = [1, 4, 9, 16, 25]
    params, fitted_values = task_func(l, x_data)
    assert params == (1.0, 0.0)
    assert fitted_values == [1.0, 4.0, 9.0, 16.0, 25.0]
    
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert params == (1.0, 0.0)
    assert fitted_values == [1.0, 4.0, 9.0, 16.0, 25.0]
    assert isinstance(ax, plt.Axes)