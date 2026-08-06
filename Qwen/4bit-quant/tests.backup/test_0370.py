import pytest
from src_0370 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple list of numbers
    data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
    ax = task_func(data)
    
    # Check if the returned object is an AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object"
    
    # Check if the histogram is plotted
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 1, "There should be one line in the plot (the histogram)"
    
    # Check if the normal distribution fit is plotted
    assert len(labels) == 1, "There should be one label in the plot (the normal distribution fit)"
    
    # Check if the title contains the correct mu and std values
    mu, std = np.mean(data), np.std(data)
    expected_title = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
    assert ax.get_title() == expected_title, "The title should contain the correct mu and std values"
    
    # Check if the plot limits are set correctly
    xmin, xmax = plt.xlim()
    assert xmin <= min(data) and xmax >= max(data), "Plot limits should include all data points"

# Run the test
if __name__ == "__main__":
    pytest.main()