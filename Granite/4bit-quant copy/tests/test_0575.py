import pytest
from src_0575 import task_func
import numpy as np

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_params():
    array_length = 200
    noise_level = 0.5
    ax = task_func(array_length, noise_level)
    assert ax is not None
    assert isinstance(ax, plt.Axes)
    x = np.linspace(0, 4*np.pi, array_length)
    y = np.sin(x) + noise_level * np.random.rand(array_length)
    popt, pcov = curve_fit(func, x, y, p0=[1, 1])
    assert np.allclose(popt[0], 1, rtol=1e-3)
    assert np.allclose(popt[1], 1, rtol=1e-3)