import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0374 import task_func


@pytest.fixture
def sample_data():
    x_data = np.array([1, 2, 3, 4, 5])
    l = np.array([2, 8, 18, 32, 50])  # This should fit a^2*x^2 + b perfectly with a=1 and b=0
    return x_data, l

def test_task_func(sample_data):
    x_data, l = sample_data
    params, fitted_values = task_func(l, x_data)
    assert len(params) == 2, "There should be two parameters (a and b)"
    assert np.allclose(fitted_values, l), "The fitted values should match the original data"

def test_task_func_plot(sample_data):
    x_data, l = sample_data
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert len(params) == 2, "There should be two parameters (a and b)"
    assert np.allclose(fitted_values, l), "The fitted values should match the original data"
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object when plotting is enabled"