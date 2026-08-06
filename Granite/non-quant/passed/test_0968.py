import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from src_0968 import task_func
import pytest

def test_task_func():
    # Test case 1: Test with a simple sine function
    def func_sine(x):
        return np.sin(x)

    ax_sine = task_func(func_sine)
    assert ax_sine is not None
    assert isinstance(ax_sine, plt.Axes)

    # Test case 2: Test with a simple cosine function
    def func_cosine(x):
        return np.cos(x)

    ax_cosine = task_func(func_cosine)
    assert ax_cosine is not None
    assert isinstance(ax_cosine, plt.Axes)

    # Test case 3: Test with a simple linear function
    def func_linear(x):
        return 2*x + 1

    ax_linear = task_func(func_linear)
    assert ax_linear is not None
    assert isinstance(ax_linear, plt.Axes)

if __name__ == "__main__":
    pytest.main()