import pytest
from src_0374 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    x_data = np.array([1, 2, 3, 4, 5])
    l = np.array([2, 8, 18, 32, 50])  # Data that fits a^x^2 + b perfectly with a=2 and b=0
    return x_data, l

def test_task_func(sample_data):
    x_data, l = sample_data
    params, fitted_values = task_func(l, x_data)
    assert len(params) == 2
    assert np.allclose(fitted_values, l), "Fitted values do not match the original data"

def test_task_func_with_plot(sample_data):
    x_data, l = sample_data
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert len(params) == 2
    assert np.allclose(fitted_values, l), "Fitted values do not match the original data"
    assert isinstance(ax, plt.Axes), "Plotting did not return an Axes object"

def test_task_func_invalid_input():
    x_data = np.array([1, 2, 3])
    l = np.array([1, 2])  # Different lengths of input arrays
    with pytest.raises(ValueError):
        task_func(l, x_data)

def test_task_func_non_numeric_input():
    x_data = [1, 2, 3]
    l = ['a', 'b', 'c']  # Non-numeric input
    with pytest.raises(TypeError):
        task_func(l, x_data)