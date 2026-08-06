import pytest
from src_0297 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import sys

# Mocking plt.show to prevent actual plotting
class Mock:
    def show(self):
        pass

plt.show = Mock().show

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_value_counts():
    data = {'value': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    expected_counts = {'A': 3, 'B': 2, 'C': 1}
    actual_counts = dict(zip(ax.get_xticklabels(), ax.get_xticks()))
    assert actual_counts == expected_counts

def test_task_func_labels_and_title():
    data = {'value': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    ax = task_func(df)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Value Distribution'

def test_task_func_no_values():
    data = {'value': []}
    df = pd.DataFrame(data)
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xticks().size == 0
    assert ax.get_yticks().size == 0

def test_task_func_single_value():
    data = {'value': ['A']}
    df = pd.DataFrame(data)
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    expected_counts = {'A': 1}
    actual_counts = dict(zip(ax.get_xticklabels(), ax.get_xticks()))
    assert actual_counts == expected_counts