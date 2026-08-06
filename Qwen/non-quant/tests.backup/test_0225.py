import pytest
from src_0225 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_invalid_range():
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=-10)

def test_task_func_default_parameters():
    data, ax, mean_fft, median_fft = task_func()
    assert isinstance(data, tuple)
    assert isinstance(ax, plt.Axes)
    assert isinstance(mean_fft, float)
    assert isinstance(median_fft, float)

def test_task_func_custom_parameters():
    data, ax, mean_fft, median_fft = task_func(range_start=-5, range_end=5, step=0.5)
    assert isinstance(data, tuple)
    assert isinstance(ax, plt.Axes)
    assert isinstance(mean_fft, float)
    assert isinstance(median_fft, float)

def test_task_func_data_generator():
    data, _, _, _ = task_func()
    for x, sin_x, cos_x, abs_x in data:
        assert isinstance(x, np.float64)
        assert isinstance(sin_x, np.float64)
        assert isinstance(cos_x, np.float64)
        assert isinstance(abs_x, np.float64)

def test_task_func_fft_values():
    _, _, mean_fft, median_fft = task_func()
    assert mean_fft >= 0
    assert median_fft >= 0

def test_task_func_plot():
    _, ax, _, _ = task_func()
    assert len(ax.collections) == 3  # 3 scatter plots for sin, cos, and abs values