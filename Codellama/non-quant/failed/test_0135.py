import pytest
from src_0135 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of B'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(None)

def test_task_func_empty_input():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_non_numeric_input():
    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e']})
    with pytest.raises(ValueError):
        task_func(df)