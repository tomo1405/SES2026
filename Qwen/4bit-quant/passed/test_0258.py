import pytest
from src_0258 import task_func
import matplotlib.pyplot as plt
import numpy as np
import math

def test_task_func():
    # Create a figure and axis for plotting
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Call the function with a sample input
    result_ax = task_func(ax, 3)

    # Check if the plot was created correctly
    assert len(result_ax.lines) == 1, "The plot should have one line"
    line = result_ax.lines[0]
    xdata, ydata = line.get_data()

    # Check if the data is correct
    expected_r = np.linspace(0, 3 * 2 * math.pi, 1000)
    expected_theta = expected_r
    assert np.allclose(xdata, expected_theta), "Theta values do not match"
    assert np.allclose(ydata, expected_r), "R values do not match"

    # Check if the rlabel position is set correctly
    assert result_ax.get_rlabel_position() == 3 * 45, "Rlabel position is incorrect"

    # Close the plot to avoid displaying it during testing
    plt.close(fig)