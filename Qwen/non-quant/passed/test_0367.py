import pytest
from src_0367 import task_func
import matplotlib.pyplot as plt
import io
import sys

def test_task_func():
    # Redirect stdout to capture any print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Prepare test data
    number_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    bins = 5
    
    # Call the function
    ax = task_func(number_list, bins)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    
    # Check if the plot has the correct title, xlabel, and ylabel
    assert ax.get_title() == 'Histogram', "The plot title should be 'Histogram'"
    assert ax.get_xlabel() == 'Number', "The x-axis label should be 'Number'"
    assert ax.get_ylabel() == 'Frequency', "The y-axis label should be 'Frequency'"
    
    # Reset redirect
    sys.stdout = sys.__stdout__

    # Optionally, you can add more checks like verifying the histogram data,
    # but since we are not modifying the target code, we will stop here.