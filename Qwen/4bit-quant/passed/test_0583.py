import pytest
from src_0583 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    # Capture the figure returned by the function
    fig = task_func()
    
    # Check if the figure is an instance of plt.Figure
    assert isinstance(fig, plt.Figure), "The function should return a matplotlib Figure object."
    
    # Check if the figure has at least one axis
    assert len(fig.axes) > 0, "The figure should contain at least one axis."
    
    # Check if the histogram is plotted on the axis
    ax = fig.axes[0]
    lines = ax.get_lines()
    assert len(lines) > 0, "The axis should contain at least one line (the normal distribution plot)."
    
    # Check if the histogram data is plotted correctly
    patches = ax.patches
    assert len(patches) > 0, "The axis should contain at least one patch (the histogram bars)."
    
    # Check if the limits of the x-axis are set correctly
    xmin, xmax = ax.get_xlim()
    assert xmin <= 0 and xmax >= 0, "The x-axis limits should include zero."
    
    # Close the figure to prevent it from being displayed
    plt.close(fig)