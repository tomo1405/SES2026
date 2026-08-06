import pytest
from src_0376 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample input data
    l = np.array([[1, 2], [3, 4], [5, 6]])

    # Call the function
    ax = task_func(l)

    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object."

    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'First Principal Component', "The x-axis label is incorrect."
    assert ax.get_ylabel() == 'Second Principal Component', "The y-axis label is incorrect."
    assert ax.get_title() == 'PCA Result', "The plot title is incorrect."

    # Check if the scatter plot has the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line (scatter plot) in the plot."
    scatter_data = lines[0].get_offsets()
    assert scatter_data.shape == (3, 2), "The scatter plot should have 3 points."

# Run the tests
if __name__ == "__main__":
    pytest.main()