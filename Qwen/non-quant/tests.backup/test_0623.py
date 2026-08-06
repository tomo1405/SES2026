import pytest
from src_0623 import task_func
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def test_task_func():
    # Prepare test data
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Call the function
    ax = task_func(L)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)
    
    # Check if the histogram is plotted
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 2  # One for the histogram and one for the PDF line
    
    # Check if the plot title contains the correct mu and std values
    title = ax.get_title()
    mu, std = norm.fit(list(chain(*L)))
    expected_title = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
    assert title == expected_title

    # Check if the PDF line is plotted correctly
    xdata, ydata = lines[1].get_data()
    pdf_x = np.linspace(min(xdata), max(xdata), 100)
    pdf_y = norm.pdf(pdf_x, mu, std)
    assert np.allclose(ydata, pdf_y, atol=1e-6)