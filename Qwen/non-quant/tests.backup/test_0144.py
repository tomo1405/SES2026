import pytest
from src_0144 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    ax = task_func()
    
    # Check if the plot has the correct title
    assert ax.get_title() == 'Solution of the equation y=2x+1 at x=2'
    
    # Check if the x and y labels are correct
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    
    # Check if the x-axis limits are set correctly
    assert ax.get_xlim() == (-10, 10)
    
    # Check if the grid is enabled
    assert ax.gridOn
    
    # Check if the legend is enabled
    assert ax.get_legend() is not None
    
    # Check if the correct lines are plotted
    lines = ax.get_lines()
    assert len(lines) == 2
    
    # Check the first line (y = 2x + 1)
    line1 = lines[0]
    xdata1, ydata1 = line1.get_data()
    np.testing.assert_array_almost_equal(xdata1, np.linspace(-10, 10, 400))
    np.testing.assert_array_almost_equal(ydata1, 2 * xdata1 + 1)
    
    # Check the second line (solution at x = 2)
    line2 = lines[1]
    xdata2, ydata2 = line2.get_data()
    assert xdata2 == [2]
    assert ydata2 == [5]  # y = 2*2 + 1 = 5
    
    # Check if the markers are correct
    assert line1.get_marker() == ''
    assert line2.get_marker() == 'o'
    
    # Check if the colors are correct
    assert line1.get_color() == 'r'
    assert line2.get_color() == 'g'
    
    # Check if the labels are correct
    assert line1.get_label() == 'y=2x+1'
    assert line2.get_label() == 'Solution at x=2'
    
    # Optionally, check if the plot can be saved to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert len(img_base64) > 0