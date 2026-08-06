import pytest
from src_1062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

@pytest.fixture
def sample_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func(sample_array):
    ax, normalized_data = task_func(sample_array)

    # Check if the returned object is a matplotlib Axes instance
    assert isinstance(ax, plt.Axes)

    # Check if the normalized data is a numpy array
    assert isinstance(normalized_data, np.ndarray)

    # Check if the shape of the normalized data is correct
    assert normalized_data.shape == (sample_array.shape[0],)

    # Check if the normalization process is correct
    row_sums = sample_array.sum(axis=1)
    mean = np.mean(row_sums)
    std_dev = np.std(row_sums)
    expected_normalized_data = (row_sums - mean) / std_dev if std_dev != 0 else np.zeros_like(row_sums)
    np.testing.assert_almost_equal(normalized_data, expected_normalized_data)

    # Check if the plot has the correct title
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"

    # Check if the plot contains the histogram and the PDF line
    lines = ax.get_lines()
    assert len(lines) == 2  # One for the histogram and one for the PDF
    assert lines[0].get_color() == 'g'  # Histogram color
    assert lines[1].get_color() == 'r'  # PDF line color