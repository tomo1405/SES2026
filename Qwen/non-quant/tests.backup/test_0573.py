import pytest
from src_0573 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Capture the plot output to ensure it's created correctly
    with plt.ioff():  # Turn off interactive mode to prevent plot display
        ax = task_func(array_length=10)

    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)

    # Check if the y-axis label is set correctly
    assert ax.get_ylabel() == 'Maximum Values'

    # Check if the plot data is correct
    max_values = np.maximum(ax.lines[0].get_ydata(), ax.lines[1].get_ydata())
    assert np.allclose(ax.lines[0].get_ydata(), max_values)

    # Check if the plot has two lines (one for each array)
    assert len(ax.lines) == 1  # Only one line should be plotted, which is the max values

    # Check if the x-axis limits are correct
    assert ax.get_xlim() == (0, 9)  # Since array_length is 10, x-axis should range from 0 to 9

# Run the test
if __name__ == "__main__":
    pytest.main()