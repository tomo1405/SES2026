import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0374 import task_func


@pytest.fixture
def sample_data():
    x_data = np.array([1, 2, 3, 4, 5])
    l = np.array([2, 5, 10, 17, 26])  # y = 2x^2 + 1
    return x_data, l

def test_task_func(sample_data):
    x_data, l = sample_data
    params, fitted_values = task_func(l, x_data)
    assert len(params) == 2, "There should be two parameters (a and b)"
    assert len(fitted_values) == len(x_data), "Fitted values should match the length of x_data"
    assert np.allclose(fitted_values, l), "Fitted values should be close to the original data"

def test_task_func_plot(sample_data):
    x_data, l = sample_data
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert len(params) == 2, "There should be two parameters (a and b)"
    assert len(fitted_values) == len(x_data), "Fitted values should match the length of x_data"
    assert np.allclose(fitted_values, l), "Fitted values should be close to the original data"
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object when plot is True"