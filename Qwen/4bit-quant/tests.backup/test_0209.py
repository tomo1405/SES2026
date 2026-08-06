import pytest
from src_0209 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_zero_input():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_non_integer_input():
    with pytest.raises(ValueError):
        task_func("string")

def test_task_func_valid_input():
    stats, ax = task_func(10)
    assert isinstance(stats, dict)
    assert set(stats.keys()) == {'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'}
    assert isinstance(ax, plt.Axes)

def test_task_func_reproducibility():
    stats1, _ = task_func(10, seed=42)
    stats2, _ = task_func(10, seed=42)
    assert stats1 == stats2

def test_task_func_plot():
    _, ax = task_func(10)
    assert ax.get_title() == 'Random Walk'
    assert len(ax.lines) == 1
    assert ax.lines[0].get_data()[0].shape == (10,)