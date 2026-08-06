import pytest
from src_0629 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    ax = task_func()
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object."
    
    # Check if the plot has the correct title
    assert ax.get_title() == 'Random Sine Wave', "The plot title should be 'Random Sine Wave'."
    
    # Check if the plot has the correct x and y labels
    assert ax.get_xlabel() == 'Time', "The x-axis label should be 'Time'."
    assert ax.get_ylabel() == 'Amplitude', "The y-axis label should be 'Amplitude'."
    
    # Check if the grid is enabled
    assert ax.gridOn, "The grid should be enabled on the plot."

# To run the tests, use the following command in your terminal:
# pytest -v