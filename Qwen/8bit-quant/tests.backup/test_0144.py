import pytest
from src_0144 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_plot():
    ax = task_func()
    
    # Check if the plot has the correct title
    assert ax.get_title() == 'Solution of the equation y=2x+1 at x=2'
    
    # Check if the plot has the correct x and y labels
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    
    # Check if the plot has the correct x-axis limits
    assert ax.get_xlim() == (-10, 10)
    
    # Check if the plot contains the line y=2x+1
    lines = ax.get_lines()
    assert len(lines) == 2  # One line for the equation and one for the solution point
    line = lines[0]
    xdata, ydata = line.get_data()
    assert np.allclose(xdata, np.linspace(-10, 10, 400))
    assert np.allclose(ydata, 2 * xdata + 1)
    
    # Check if the plot contains the solution point at (2, 5)
    solution_point = lines[1]
    xdata, ydata = solution_point.get_data()
    assert np.allclose(xdata, [2])
    assert np.allclose(ydata, [5])
    
    # Check if the plot has a legend
    legend = ax.get_legend()
    assert legend is not None
    
    # Check if the grid is enabled
    assert ax.gridOn

def test_task_func_plot_output():
    ax = task_func()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert img_base64  # Ensure that the image is not empty