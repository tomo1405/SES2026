import pytest
from src_0464 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_with_default_separator_and_bins():
    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str)
    assert isinstance(data, pd.Series)
    assert data.equals(pd.Series([1, 2, 3, 4, 5], dtype='int64'))
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_separator_and_bins():
    data_str = "1;2;3;4;5"
    data, ax = task_func(data_str, separator=";", bins=10)
    assert isinstance(data, pd.Series)
    assert data.equals(pd.Series([1, 2, 3, 4, 5], dtype='int64'))
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_data_str():
    data_str = ""
    with pytest.raises(ValueError, match="Failed to find valid data"):
        task_func(data_str)

def test_task_func_with_non_numeric_data():
    data_str = "1,2,a,4,5"
    with pytest.raises(ValueError, match="Failed to find valid data"):
        task_func(data_str)

def test_task_func_with_single_value():
    data_str = "42"
    data, ax = task_func(data_str)
    assert isinstance(data, pd.Series)
    assert data.equals(pd.Series([42], dtype='int64'))
    assert isinstance(ax, plt.Axes)