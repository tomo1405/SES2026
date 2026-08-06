import matplotlib.pyplot as plt
import numpy as np
from src_0629 import task_func


def test_task_func():
    ax = task_func()
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object."
    
    # Check if the plot has the correct title, xlabel, and ylabel
    assert ax.get_title() == 'Random Sine Wave', "The plot title should be 'Random Sine Wave'."
    assert ax.get_xlabel() == 'Time', "The x-axis label should be 'Time'."
    assert ax.get_ylabel() == 'Amplitude', "The y-axis label should be 'Amplitude'."
    
    # Check if the grid is enabled
    assert ax.gridOn, "The grid should be enabled on the plot."
    
    # Check if the data points are within the expected range
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be only one line in the plot."
    xdata, ydata = lines[0].get_data()
    assert np.allclose(xdata, np.arange(0, 10, 0.01), atol=1e-2), "X data should be in the range [0, 10] with step 0.01."
    assert np.max(np.abs(ydata)) <= 5, "Y data should have an amplitude of at most 5."
    assert np.min(ydata) >= -5, "Y data should have an amplitude of at least -5."

    # Check if the phase shift is within the expected range
    phase_shift = ax.phase_shift  # Assuming phase_shift is stored in the ax object
    assert 0 <= phase_shift <= 360, "Phase shift should be between 0 and 360 degrees."