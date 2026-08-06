import pytest
from src_1037 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_series():
    s1 = pd.Series(np.random.randn(10), name='Series1')
    s2 = pd.Series(np.random.randn(10), name='Series2')
    return s1, s2

def test_task_func_returns_correct_types(sample_series):
    s1, s2 = sample_series
    ax, intersection_count = task_func(s1, s2)
    assert isinstance(ax, plt.Axes)
    assert isinstance(intersection_count, int)

def test_task_func_intersection_count(sample_series):
    s1, s2 = sample_series
    intersection_count = len(set(s1).intersection(set(s2)))
    ax, returned_intersection_count = task_func(s1, s2)
    assert intersection_count == returned_intersection_count

def test_task_func_plot_title(sample_series):
    s1, s2 = sample_series
    ax, _ = task_func(s1, s2)
    expected_title = f"Overlap Between {s1.name} and {s2.name}"
    assert ax.get_title() == expected_title

def test_task_func_highlight_intersection(sample_series):
    s1, s2 = sample_series
    intersection = set(s1).intersection(set(s2))
    ax, _ = task_func(s1, s2)
    lines = [line for line in ax.get_lines() if line.get_linestyle() == '--' and line.get_color() == 'red']
    assert len(lines) == len(intersection)