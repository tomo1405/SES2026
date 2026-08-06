import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from src_0968 import task_func
import pytest

def test_task_func():
    # Test case 1: Test with a simple function
    def func1(x):
        return x**2

    ax1 = task_func(func1)
    assert ax1 is not None
    assert isinstance(ax1, plt.Axes)

    # Test case 2: Test with a more complex function
    def func2(x):
        return np.sin(x) + np.cos(x**2)

    ax2 = task_func(func2)
    assert ax2 is not None
    assert isinstance(ax2, plt.Axes)

    # Test case 3: Test with a function that raises an exception
    def func3(x):
        raise ValueError("Test exception")

    with pytest.raises(ValueError):
        task_func(func3)