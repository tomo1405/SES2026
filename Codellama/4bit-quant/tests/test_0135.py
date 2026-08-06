import matplotlib
import pandas as pd
import pytest
from src_0135 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    ax = task_func(df)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Histogram of B'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (1, 6)
    assert ax.get_ylim() == (0, 3)

def test_task_func_with_bins():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    ax = task_func(df, bins=5)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Histogram of B'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (1, 6)
    assert ax.get_ylim() == (0, 3)

def test_task_func_with_invalid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df, bins=0)