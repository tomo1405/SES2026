import pytest
from src_0968 import task_func
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

@pytest.fixture
def simple_func():
    def f(x):
        return x**2
    return f

def test_task_func_output(simple_func):
    ax = task_func(simple_func, x_range=(-2, 2), num_points=1000)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot_data(simple_func):
    ax = task_func(simple_func, x_range=(-2, 2), num_points=1000)
    lines = ax.get_lines()
    assert len(lines) == 2

    # Check the first line (original function)
    x_data, y_data = lines[0].get_data()
    expected_y_data = np.array([simple_func(x) for x in x_data])
    assert np.allclose(y_data, expected_y_data)

    # Check the second line (integral)
    x_data, y_data = lines[1].get_data()
    expected_y_data = integrate.cumulative_trapezoid(expected_y_data, x_data, initial=0)
    assert np.allclose(y_data, expected_y_data)

def test_task_func_legend_labels(simple_func):
    ax = task_func(simple_func, x_range=(-2, 2), num_points=1000)
    legend_texts = [text.get_text() for text in ax.get_legend().get_texts()]
    expected_labels = [f"{simple_func.__name__}(x)", f"Integral of {simple_func.__name__}(x)"]
    assert legend_texts == expected_labels

def test_task_func_with_different_x_range(simple_func):
    ax = task_func(simple_func, x_range=(0, 4), num_points=1000)
    x_data = ax.get_lines()[0].get_data()[0]
    assert np.isclose(x_data.min(), 0)
    assert np.isclose(x_data.max(), 4)

def test_task_func_with_different_num_points(simple_func):
    ax = task_func(simple_func, x_range=(-2, 2), num_points=500)
    x_data = ax.get_lines()[0].get_data()[0]
    assert len(x_data) == 500