python
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import pytest

def task_func(func, x_range=(-2, 2), num_points=1000):
    X = np.linspace(x_range[0], x_range[1], num_points)
    y = func(X)
    y_int = integrate.cumulative_trapezoid(y, X, initial=0)

    fig, ax = plt.subplots()
    ax.plot(X, y, label=f"{func.__name__}(x)")
    ax.plot(X, y_int, label=f"Integral of {func.__name__}(x)")
    ax.legend()

    return ax

def test_task_func():
    def f(x):
        return np.sin(x)

    ax = task_func(f)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Integral of f(x)'
    assert ax.get_legend().get_texts()[0].get_text() == 'f(x)'
    assert ax.get_legend().get_texts()[1].get_text() == 'Integral of f(x)'
    assert ax.get_legend().get_lines()[0].get_data()[0].shape == (1000,)
    assert ax.get_legend().get_lines()[1].get_data()[0].shape == (1000,)