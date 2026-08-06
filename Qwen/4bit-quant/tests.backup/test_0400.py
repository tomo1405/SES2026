import pytest
from src_0400 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_frequency():
    frequency = 5
    sample_size = 10000
    fig, ax = task_func(frequency, sample_size)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

def test_task_func_zero_frequency():
    with pytest.raises(ValueError, match="Frequency cannot be negative"):
        task_func(-1, 10000)

def test_task_func_negative_sample_size():
    with pytest.raises(ValueError, match="Sample size cannot be negative or zero"):
        task_func(5, -10000)

def test_task_func_zero_sample_size():
    with pytest.raises(ValueError, match="Sample size cannot be negative or zero"):
        task_func(5, 0)

def test_task_func_default_sample_size():
    frequency = 3
    fig, ax = task_func(frequency)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot_data():
    frequency = 2
    sample_size = 10
    fig, ax = task_func(frequency, sample_size)
    lines = ax.get_lines()
    assert len(lines) == 2
    x_data = lines[0].get_xdata()
    y_sin_data = lines[0].get_ydata()
    y_cos_data = lines[1].get_ydata()
    assert np.array_equal(x_data, np.linspace(0, 2 * np.pi, sample_size))
    assert np.allclose(y_sin_data, np.sin(frequency * x_data))
    assert np.allclose(y_cos_data, np.cos(frequency * x_data))