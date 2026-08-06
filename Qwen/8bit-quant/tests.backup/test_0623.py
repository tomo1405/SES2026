import pytest
from src_0623 import task_func
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def test_task_func():
    # Prepare test data
    L = [[1, 2, 3], [4, 5, 6]]
    
    # Call the function
    ax = task_func(L)
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the histogram was plotted
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 1  # Only one line should be in the plot (the normal distribution curve)
    assert labels[0] == 'k'  # The line color should be black
    
    # Check if the histogram data is correct
    data = list(chain(*L))
    bins, _ = np.histogram(data, bins=30, density=True)
    bars = ax.patches
    assert len(bars) == 30  # There should be 30 bars in the histogram
    for i, bar in enumerate(bars):
        assert np.isclose(bar.get_height(), bins[i])  # Heights of the bars should match the histogram data
    
    # Check if the normal distribution curve is correct
    mu, std = norm.fit(data)
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    line = lines[0]
    assert np.allclose(line.get_xdata(), x)  # X data of the line should match the x values
    assert np.allclose(line.get_ydata(), p)  # Y data of the line should match the PDF values
    
    # Check if the title is correct
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    assert ax.get_title() == title

# To run the tests, use the command: pytest -v