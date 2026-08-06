import pytest
from src_0896 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_output():
    array, mean, std, ax = task_func()
    
    # Check if the array has the correct size
    assert len(array) == 10000, "Array size is incorrect"
    
    # Check if the mean and std are within expected range
    assert 1 <= mean <= 500, "Mean value is out of expected range"
    assert 0 <= std <= 250, "Standard deviation value is out of expected range"
    
    # Check if the ax object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "ax is not a matplotlib AxesSubplot"

def test_task_func_histogram():
    array, _, _, ax = task_func()
    
    # Get the histogram data from the ax object
    n, bins, patches = ax.get_histgram()
    
    # Check if the number of bins is appropriate
    assert len(bins) > 1, "Number of bins is too low"
    
    # Check if the sum of frequencies equals the array size
    assert np.sum(n) == 10000, "Sum of frequencies does not match array size"

def test_task_func_plot_labels():
    _, _, _, ax = task_func()
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Histogram of Random Values', "Title is incorrect"
    assert ax.get_xlabel() == 'Val', "X-axis label is incorrect"
    assert ax.get_ylabel() == 'Freq', "Y-axis label is incorrect"