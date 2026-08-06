python
import pytest
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

def test_task_func():
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]
    popt, ax = task_func(X, Y)
    assert popt == [1.0, 1.0, 1.0]
    assert ax.get_xlabel() == 'X'
    assert ax.get_ylabel() == 'Y'
    assert ax.get_title() == 'Fitted Curve'
    assert ax.get_xlim() == (1, 5)
    assert ax.get_ylim() == (1, 11)
    assert ax.get_xticks() == [1, 2, 3, 4, 5]
    assert ax.get_yticks() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.close()