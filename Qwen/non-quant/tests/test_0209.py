import pytest
from src_0209 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func("string")

def test_task_func_output_type():
    stats, ax = task_func(10)
    assert isinstance(stats, dict)
    assert isinstance(ax, plt.Axes)

def test_task_func_descriptive_stats_keys():
    stats, _ = task_func(10)
    expected_keys = ['count', 'mean', 'std', 'min', '5%', '25%', '50%', '75%', '95%', 'max']
    assert set(stats.keys()) == set(expected_keys)

def test_task_func_descriptive_stats_values():
    stats, _ = task_func(10, seed=42)
    expected_stats = {
        'count': 10.0,
        'mean': 0.0,
        'std': 1.0,
        'min': -1.0,
        '5%': -1.0,
        '25%': -1.0,
        '50%': 0.0,
        '75%': 1.0,
        '95%': 1.0,
        'max': 1.0
    }
    assert stats == expected_stats

def test_task_func_plot():
    _, ax = task_func(10)
    assert ax.get_title() == 'Random Walk'
    assert len(ax.lines) == 1
    assert ax.lines[0].get_data()[0].size == 10
    assert ax.figure.canvas.get_width_height() == (800, 600)

def test_task_func_reproducibility():
    stats1, _ = task_func(10, seed=42)
    stats2, _ = task_func(10, seed=42)
    assert stats1 == stats2