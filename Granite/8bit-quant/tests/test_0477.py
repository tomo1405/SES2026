import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(X, Y):

    def func(x, a, b, c):
        return a * x ** 2 + b * x + c

    popt, pcov = curve_fit(func, X, Y)

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, func(X, *popt), "r-")

    return list(popt), ax
import pytest

def test_task_func():
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 2]
    popt, ax = task_func(X, Y)
    assert len(popt) == 3
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input():
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4]
    with pytest.raises(ValueError):
        task_func(X, Y)