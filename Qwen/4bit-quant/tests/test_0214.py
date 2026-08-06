import time

import matplotlib.pyplot as plt
import pytest
from src_0214 import task_func


def test_task_func_default():
    ax, kurtosis_value = task_func(intervals=5, seed=42)
    assert isinstance(ax, plt.Axes)
    assert isinstance(kurtosis_value, float)

def test_task_func_with_zero_intervals():
    ax, kurtosis_value = task_func(intervals=0, seed=42)
    assert isinstance(ax, plt.Axes)
    assert isinstance(kurtosis_value, float)
    assert len(ax.lines[0].get_xdata()) == 0
    assert len(ax.lines[0].get_ydata()) == 0

def test_task_func_with_negative_intervals():
    with pytest.raises(ValueError):
        task_func(intervals=-1, seed=42)

def test_task_func_with_large_intervals():
    ax, kurtosis_value = task_func(intervals=10, seed=42)
    assert isinstance(ax, plt.Axes)
    assert isinstance(kurtosis_value, float)
    assert len(ax.lines[0].get_xdata()) == 10
    assert len(ax.lines[0].get_ydata()) == 10

def test_task_func_with_keyboard_interrupt():
    def mock_sleep(seconds):
        raise KeyboardInterrupt

    with pytest.raises(KeyboardInterrupt):
        with pytest.monkeypatch.context() as mp:
            mp.setattr(time, 'sleep', mock_sleep)
            task_func(intervals=5, seed=42)