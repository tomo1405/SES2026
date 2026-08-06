import pytest
from src_1063 import task_func
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

@pytest.fixture
def empty_array():
    return np.array([])

@pytest.fixture
def sample_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func_empty_array(empty_array):
    ax = task_func(empty_array)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Time Series of Row Sums"

def test_task_func_sample_array(sample_array):
    ax = task_func(sample_array)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    
    expected_dates = pd.date_range(start="1/1/2020", periods=3)
    actual_dates = ax.lines[0].get_xdata()
    
    assert all(expected_dates == actual_dates)
    
    expected_sums = np.array([6, 15, 24])
    actual_sums = ax.lines[0].get_ydata()
    
    assert all(expected_sums == actual_sums)