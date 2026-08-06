import pytest
from src_0625 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple 3x3 matrix
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    pca_result, ax = task_func(L)

    # Check that the PCA result is a 2D array with the correct shape
    assert isinstance(pca_result, np.ndarray)
    assert pca_result.shape == (3, 2)

    # Check that the axes object is of the correct type
    assert isinstance(ax, plt.Axes)

    # Check that the plot contains the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert len(xdata) == 3
    assert len(ydata) == 3

    # Clean up the plot
    plt.close(fig)