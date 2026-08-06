import pytest
from src_0629 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    ax = task_func()
    
    # Check if the plot is created with the correct title and labels
    assert ax.get_title() == 'Random Sine Wave'
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Amplitude'
    
    # Check if the grid is enabled
    assert ax.gridOn
    
    # Check if the returned object is an AxesSubplot instance
    assert isinstance(ax, plt.Axes)

    # Check if the plot contains data
    lines = ax.get_lines()
    assert len(lines) == 1  # There should be one line plot
    
    # Extract the data from the plot
    x_data, y_data = lines[0].get_data()
    
    # Check if x_data has 1000 points
    assert len(x_data) == 1000
    
    # Check if y_data is within the expected range based on amplitude
    amplitude = np.max(np.abs(y_data))
    assert amplitude <= 5  # Maximum amplitude should not exceed 5

# Run the test
if __name__ == "__main__":
    pytest.main()