import pytest
from src_0896 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    array, mean, std, ax = task_func()

    # Check that the array has the correct size
    assert len(array) == 10000

    # Check that the mean and standard deviation are within a reasonable range
    assert 1 <= mean <= 500
    assert 0 <= std < 250

    # Check that the plot is correctly configured
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of Random Values'
    assert ax.get_xlabel() == 'Val'
    assert ax.get_ylabel() == 'Freq'

    # Check that the histogram data matches the array
    hist_data, _ = ax.get_lines()[0].get_data()
    assert np.allclose(hist_data, np.histogram(array, bins='auto')[0])

    # Close the plot to avoid it showing up during tests
    plt.close(fig)