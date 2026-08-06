import pytest
from src_0356 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Define parameters
    amplitude = 1.0
    frequency = 1.0
    time = np.linspace(0, 1, 100)

    # Call the function
    wave, fig, ax = task_func(amplitude, frequency, time)

    # Check the output types
    assert isinstance(wave, np.ndarray), "The wave should be a numpy array"
    assert isinstance(fig, plt.Figure), "The figure should be a matplotlib Figure"
    assert isinstance(ax, plt.Axes), "The axes should be a matplotlib Axes"

    # Check the plot
    assert len(ax.lines) == 2, "There should be two lines in the plot"
    assert ax.get_title() == "Complex Wave with Hann Window", "The plot title is incorrect"

    # Close the plot to avoid displaying it during testing
    plt.close()