from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0497 import task_func


def test_task_func_default():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.get_lines()[0].get_xdata()) == 7
    assert len(ax.get_lines()[0].get_ydata()) == 7

def test_task_func_custom_days():
    ax = task_func(days_in_past=5)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.get_lines()[0].get_xdata()) == 5
    assert len(ax.get_lines()[0].get_ydata()) == 5

def test_task_func_custom_random_seed():
    ax1 = task_func(random_seed=1)
    ax2 = task_func(random_seed=1)
    assert np.array_equal(ax1.get_lines()[0].get_ydata(), ax2.get_lines()[0].get_ydata())

def test_task_func_invalid_days():
    with pytest.raises(ValueError, match="days_in_past must be in the past"):
        task_func(days_in_past=0)

def test_task_func_dates_correctness():
    ax = task_func(days_in_past=3)
    current_date = datetime.now().date()
    expected_dates = [current_date - timedelta(days=i) for i in range(3)]
    assert list(ax.get_lines()[0].get_xdata()) == expected_dates

def test_task_func_temperature_range():
    ax = task_func()
    temperatures = ax.get_lines()[0].get_ydata()
    assert all(15 <= temp < 35 for temp in temperatures)