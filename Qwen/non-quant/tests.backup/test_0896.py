import pytest
from src_0896 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_return_values():
    array, mean, std, ax = task_func()
    
    # Check if the array has the correct size
    assert len(array) == 10000
    
    # Check if the mean is a float
    assert isinstance(mean, float)
    
    # Check if the standard deviation is a float
    assert isinstance(std, float)
    
    # Check if ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)

def test_task_func_array_values():
    array, _, _, _ = task_func()
    
    # Check if all values in the array are within the expected range
    assert np.all(array >= 1) and np.all(array < 500)

def test_task_func_plot():
    _, _, _, ax = task_func()
    
    # Check if the plot has the correct title
    assert ax.get_title() == 'Histogram of Random Values'
    
    # Check if the plot has the correct x-label
    assert ax.get_xlabel() == 'Val'
    
    # Check if the plot has the correct y-label
    assert ax.get_ylabel() == 'Freq'