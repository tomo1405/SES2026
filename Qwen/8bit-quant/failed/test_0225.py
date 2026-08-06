import pytest
from src_0225 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def test_task_func_default_values():
    data, ax, mean_fft, median_fft = task_func()
    x_values = np.arange(-10, 10, 0.1)
    expected_mean_fft = abs(np.mean(fft([abs(np.sin(x) - np.cos(x)) for x in x_values])))
    expected_median_fft = abs(np.median(fft([abs(np.sin(x) - np.cos(x)) for x in x_values])))
    assert isinstance(data, list)
    assert isinstance(ax, plt.Axes)
    assert np.isclose(mean_fft, expected_mean_fft)
    assert np.isclose(median_fft, expected_median_fft)

def test_task_func_custom_range():
    data, ax, mean_fft, median_fft = task_func(range_start=0, range_end=5, step=0.5)
    x_values = np.arange(0, 5, 0.5)
    expected_mean_fft = abs(np.mean(fft([abs(np.sin(x) - np.cos(x)) for x in x_values])))
    expected_median_fft = abs(np.median(fft([abs(np.sin(x) - np.cos(x)) for x in x_values])))
    assert isinstance(data, list)
    assert isinstance(ax, plt.Axes)
    assert np.isclose(mean_fft, expected_mean_fft)
    assert np.isclose(median_fft, expected_median_fft)

def test_task_func_invalid_range():
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=-10)

def test_task_func_step_zero():
    with pytest.raises(ValueError):
        task_func(step=0)

def test_task_func_step_negative():
    with pytest.raises(ValueError):
        task_func(step=-0.1)