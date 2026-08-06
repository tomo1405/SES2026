import pytest
from src_0209 import task_func
import numpy as np
import pandas as pd

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func("string")
    with pytest.raises(ValueError):
        task_func(3.5)

def test_task_func_valid_input():
    descriptive_stats, ax = task_func(10)
    assert isinstance(descriptive_stats, dict)
    assert 'count' in descriptive_stats
    assert 'mean' in descriptive_stats
    assert 'std' in descriptive_stats
    assert 'min' in descriptive_stats
    assert '25%' in descriptive_stats
    assert '50%' in descriptive_stats
    assert '75%' in descriptive_stats
    assert 'max' in descriptive_stats
    assert '5%' in descriptive_stats
    assert '95%' in descriptive_stats
    assert isinstance(ax, plt.Axes)

def test_task_func_reproducibility():
    stats1, _ = task_func(10, seed=42)
    stats2, _ = task_func(10, seed=42)
    assert stats1 == stats2

def test_task_func_random_walk_length():
    _, ax = task_func(10)
    x_data, y_data = ax.get_lines()[0].get_data()
    assert len(x_data) == 10
    assert len(y_data) == 10