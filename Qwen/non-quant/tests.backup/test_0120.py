import pytest
from src_0120 import task_func
import matplotlib.pyplot as plt
import io
import sys

def test_task_func_plot():
    # Redirect stdout to capture any print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Capture the current state of the figure before running the function
    initial_figures = plt.get_fignums()
    
    # Run the function
    task_func()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check that no print statements were made
    assert captured_output.getvalue() == ""
    
    # Check that a new figure was created
    final_figures = plt.get_fignums()
    assert len(final_figures) == len(initial_figures) + 1
    
    # Get the last created figure
    fig = plt.figure(final_figures[-1])
    ax = fig.axes[0]
    
    # Check the title
    assert ax.get_title() == 'y = x^2'
    
    # Check the labels
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    
    # Check the grid
    assert ax.gridOn
    
    # Check the data
    lines = ax.get_lines()
    assert len(lines) == 1
    x_data, y_data = lines[0].get_data()
    assert np.array_equal(x_data, np.linspace(-10, 10, 400))
    assert np.array_equal(y_data, x_data**2)

# To run the test, use the command: pytest -v