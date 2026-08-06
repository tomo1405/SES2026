import pytest
from src_0464 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_with_valid_data():
    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str)
    assert isinstance(data, pd.Series)
    assert data.dtype == 'int64'
    assert len(data) == 5
    assert all(data == [1, 2, 3, 4, 5])
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_data():
    data_str = ""
    with pytest.raises(ValueError) as excinfo:
        task_func(data_str)
    assert str(excinfo.value) == "Failed to find valid data"

def test_task_func_with_custom_separator():
    data_str = "1;2;3;4;5"
    data, ax = task_func(data_str, separator=";")
    assert isinstance(data, pd.Series)
    assert data.dtype == 'int64'
    assert len(data) == 5
    assert all(data == [1, 2, 3, 4, 5])
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_bins():
    data_str = "1,2,3,4,5,6,7,8,9,10"
    data, ax = task_func(data_str, bins=5)
    assert isinstance(data, pd.Series)
    assert data.dtype == 'int64'
    assert len(data) == 10
    assert all(data == list(range(1, 11)))
    assert isinstance(ax, plt.Axes)

def test_task_func_with_negative_numbers():
    data_str = "-1,-2,-3,-4,-5"
    data, ax = task_func(data_str)
    assert isinstance(data, pd.Series)
    assert data.dtype == 'int64'
    assert len(data) == 5
    assert all(data == [-1, -2, -3, -4, -5])
    assert isinstance(ax, plt.Axes)

def test_task_func_with_float_numbers():
    data_str = "1.0,2.0,3.0,4.0,5.0"
    with pytest.raises(ValueError) as excinfo:
        task_func(data_str)
    assert str(excinfo.value) == "Failed to find valid data"