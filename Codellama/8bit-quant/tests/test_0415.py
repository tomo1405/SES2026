import matplotlib
import pandas as pd
from src_0415 import task_func


def test_task_func_with_valid_data():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_with_invalid_data():
    data = pd.DataFrame({"a": ["a", "b", "c"], "b": ["d", "e", "f"]})
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert ax is None

def test_task_func_with_empty_data():
    data = pd.DataFrame()
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert ax is None

def test_task_func_with_non_numeric_data():
    data = pd.DataFrame({"a": ["a", "b", "c"], "b": ["d", "e", "f"]})
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert ax is None