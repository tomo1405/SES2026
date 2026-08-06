import pytest
from src_0144 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Call the function to generate the plot
    ax = task_func()
    
    # Check if the plot has the correct title
    assert ax.get_title() == 'Solution of the equation y=2x+1 at x=2'
    
    # Check if the plot has the correct x and y labels
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    
    # Check if the x-axis limits are set correctly
    assert ax.get_xlim() == (-10, 10)
    
    # Check if the legend is enabled
    legend = ax.get_legend()
    assert legend is not None
    
    # Check if the grid is enabled
    assert ax.get_xgrid() == True
    assert ax.get_ygrid() == True
    
    # Check if the correct lines and markers are plotted
    lines = ax.get_lines()
    assert len(lines) == 2  # One for the line, one for the marker
    
    # Check the line equation y = 2x + 1
    x_values = np.linspace(-10, 10, 400)
    y_values = 2 * x_values + 1
    line_data = lines[0].get_data()
    assert np.allclose(line_data[0], x_values)
    assert np.allclose(line_data[1], y_values)
    
    # Check the marker at x = 2
    marker_data = lines[1].get_data()
    assert marker_data[0] == [2]
    assert marker_data[1] == [5]  # y value at x = 2 is 5