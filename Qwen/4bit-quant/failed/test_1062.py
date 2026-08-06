import pytest
import numpy as np
from src_1062 import task_func

def test_task_func():
    # Create a sample input array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Call the function
    ax, normalized_data = task_func(arr)

    # Check the shape of the normalized data
    assert normalized_data.shape == (arr.shape[0],), "Normalized data should have the same number of rows as the input array"

    # Check that the normalized data is a numpy array
    assert isinstance(normalized_data, np.ndarray), "Normalized data should be a numpy array"

    # Check that the plot axis is returned
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

    # Check that the histogram and PDF are plotted
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be one line (PDF) in the plot"
    patches = ax.patches
    assert len(patches) == 30, "There should be 30 bins in the histogram"

    # Check that the title is set correctly
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF", "The plot title is incorrect"

    # Check that the mean of the normalized data is close to 0
    assert np.isclose(np.mean(normalized_data), 0, atol=1e-6), "Mean of normalized data should be close to 0"

    # Check that the standard deviation of the normalized data is close to 1
    assert np.isclose(np.std(normalized_data), 1, atol=1e-6), "Standard deviation of normalized data should be close to 1"