import pytest
from src_0497 import task_func
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == 7
    assert len(ax.lines[0].get_ydata()) == 7

def test_task_func_custom_days_in_past():
    ax = task_func(days_in_past=5)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == 5
    assert len(ax.lines[0].get_ydata()) == 5

def test_task_func_custom_random_seed():
    ax1 = task_func(random_seed=123)
    ax2 = task_func(random_seed=123)
    assert np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())

def test_task_func_invalid_days_in_past():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

def test_task_func_plot_labels():
    ax = task_func()
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Temperature (°C)"
    assert ax.get_title() == "Temperature Trend"

def test_task_func_dates_order():
    ax = task_func(days_in_past=3)
    dates = ax.lines[0].get_xdata()
    assert dates[0] > dates[1] > dates[2]

def test_task_func_temperature_range():
    ax = task_func(days_in_past=3)
    temperatures = ax.lines[0].get_ydata()
    assert all(15 <= temp <= 35 for temp in temperatures)