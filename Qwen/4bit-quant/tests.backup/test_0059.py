import pytest
from src_0059 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Mocking the plt.show() to prevent GUI display during testing
    plt.show = lambda: None
    
    # Define test parameters
    mu = 0
    sigma = 1
    num_samples = 1000
    
    # Call the function
    fig = task_func(mu, sigma, num_samples)
    
    # Check if the figure is created
    assert isinstance(fig, plt.Figure), "The function should return a matplotlib Figure object."
    
    # Check if the histogram is plotted correctly
    ax = fig.axes[0]
    hist_data, _ = ax.get_lines()[0].get_data()
    assert len(hist_data) > 0, "The histogram data should not be empty."
    
    # Check if the normal distribution curve is plotted correctly
    line_data, _ = ax.get_lines()[1].get_data()
    assert len(line_data) > 0, "The normal distribution curve data should not be empty."
    
    # Check if the title is set correctly
    assert ax.get_title() == 'Normal Distribution', "The plot title should be 'Normal Distribution'."