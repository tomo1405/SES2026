import pytest
from src_0135 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of b'
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
    df = pd.DataFrame({'a': ['a', 'b', 'c', 'd', 'e']})
    with pytest.raises(ValueError):
        task_func(df)