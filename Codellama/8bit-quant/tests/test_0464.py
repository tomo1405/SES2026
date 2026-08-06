import pytest
from src_0464 import task_func
import numpy as np
import pandas as pd

def test_task_func_valid_data():
    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str)
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, pd.Series)
    assert data.size == 5
    assert ax.size == 5

def test_task_func_invalid_data():
    data_str = ""
    with pytest.raises(ValueError):
        task_func(data_str)

def test_task_func_custom_separator():
    data_str = "1|2|3|4|5"
    data, ax = task_func(data_str, separator="|")
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, pd.Series)
    assert data.size == 5
    assert ax.size == 5

def test_task_func_custom_bins():
    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, bins=10)
    assert isinstance(data, np.ndarray)
    assert isinstance(ax, pd.Series)
    assert data.size == 5
    assert ax.size == 10