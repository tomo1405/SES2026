import pytest
from src_0101 import task_func
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime

def test_task_func():
    # Capture the current state of the random number generator
    original_state = random.getstate()
    
    # Call the function with a fixed seed
    ax = task_func(seed=42)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object."
    
    # Check if the plot has the correct number of data points
    assert len(ax.lines[0].get_xdata()) == 30, "The plot should have 30 data points."
    assert len(ax.lines[0].get_ydata()) == 30, "The plot should have 30 data points."
    
    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'Date', "The x-axis label should be 'Date'."
    assert ax.get_ylabel() == 'Value', "The y-axis label should be 'Value'."
    assert ax.get_title() == 'Random Time Series Data', "The plot title should be 'Random Time Series Data'."
    
    # Check if the plot has the legend
    assert ax.get_legend() is not None, "The plot should have a legend."
    
    # Restore the original state of the random number generator
    random.setstate(original_state)

def test_task_func_exception():
    # Test the exception handling by passing a non-integer seed
    with pytest.raises(ValueError, match="Error generating the plot"):
        task_func(seed="invalid_seed")